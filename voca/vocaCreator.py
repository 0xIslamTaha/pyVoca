import requests, os
from bs4 import BeautifulSoup
from termcolor import colored
from voca.vocaDict import vocaDict
from voca.vocaUtil import vocaUtil

class vocaCreator(vocaUtil):
    def __init__(self):
        self.refrance_url = 'https://www.vocabulary.com/dictionary/%s'
        self.sentence_url = 'http://sentence.yourdictionary.com/%s'
        self.write_dict_flag = False
        self.short = ''
        self.long = ''
        self.sentences = []

    def looking_for_list(self, SEARCH_LIST):
        if SEARCH_LIST:
            for word in SEARCH_LIST:
                word = word.lower()
                short_text, long_text, sentences = self.check_word_in_local_dect(word)
                if not short_text:
                    self.short, self.long = self.get_description(word)
                    if not self.short:
                        continue
                    self.sentences = self.get_sentences(word)
                    self.update_dict(word, self.short, self.long, self.sentences)
                else:
                    self.print_short_description(word, short_text)
                    self.print_long_description(long_text)
                    self.print_sentences(sentences)
            if self.write_dict_flag:
                self.write_dict()

    def get_description(self, word):
        self.write_dict_flag = True
        content = requests.get(url=self.refrance_url % word).content
        soup = BeautifulSoup(content, 'lxml')
        short = self.get_short_description(word, soup)
        long = self.get_long_description(soup)
        return short, long

    def get_sentences(self, word):
        sentences = []
        content = requests.get(url=self.sentence_url % word).content
        soup = BeautifulSoup(content, 'lxml')
        data = soup.findAll('div', attrs={'class': 'li_content'})
        if data:
            for index in range(3):
                sentence = data[index].getText()
                sentences.append(sentence)
            vocaCreator.print_sentences(sentences)
            return sentences

    @staticmethod
    def get_short_description(word, soup):
        short = soup.findAll('p', attrs={'class': 'short'})
        if short:
            short_text = short[0].getText()
            vocaCreator.print_short_description(word, short_text)
            return short_text
        else:
            print(colored(' * There is no description :( !!', 'red'))

    @staticmethod
    def get_long_description(soup):
        long = soup.findAll('p', attrs={'class': 'long'})
        if long:
            long_text = long[0].getText()
            vocaCreator.print_long_description(long_text)
            return long_text

    @staticmethod
    def update_dict(word, short, long, sentences):
        vocaDict[word] = {'short': short,
                          'long': long,
                          'sentences': sentences}

    @staticmethod
    def write_dict():
        script_dir = os.path.dirname(__file__)
        voca_path = os.path.join(script_dir, 'vocaDict.py')
        tmp = open(voca_path, 'w')
        tmp.write('vocaDict = %s' % str(vocaDict))
        tmp.close()
