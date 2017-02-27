import requests, os
from bs4 import BeautifulSoup
from termcolor import colored
from voca.vocaDict import vocaDict


class vocaCreatro:
    def __init__(self):
        self.refrance_url = 'https://www.vocabulary.com/dictionary/%s'
        self.write_dict_flag = False
        self.short = ''
        self.long = ''

    def looking_for_list(self, SEARCH_LIST):
        if SEARCH_LIST:
            for word in SEARCH_LIST:
                word = word.lower()
                short_text, long_text = self.check_word_in_local_dect(word)
                if not short_text:
                    self.write_dict_flag = True
                    content = requests.get(url=self.refrance_url % word).content
                    soup = BeautifulSoup(content, 'lxml')
                    self.short = self.get_short_description(word, soup)
                    self.long = self.get_long_description(soup)
                    if not self.short:
                        continue
                    self.update_dict(word, self.short, self.long)
                else:
                    self.print_short_description(word, short_text)
                    self.print_long_description(long_text)

            if self.write_dict_flag:
                self.write_dict()

    @staticmethod
    def check_word_in_local_dect(word):
        if word in vocaDict:
            return vocaDict[word]['short'], vocaDict[word]['long']
        else:
            return None, None

    @staticmethod
    def get_short_description(word, soup):
        short = soup.findAll('p', attrs={'class': 'short'})
        if short:
            short_text = short[0].getText()
            vocaCreatro.print_short_description(word, short_text)
            return short_text
        else:
            print(colored(' * There is no description :( !!', 'red'))

    @staticmethod
    def get_long_description(soup):
        long = soup.findAll('p', attrs={'class': 'long'})
        if long:
            long_text = long[0].getText()
            vocaCreatro.print_long_description(long_text)
            return long_text

    @staticmethod
    def update_dict(word, short, long):
        vocaDict[word] = {'short': short,
                          'long': long}

    @staticmethod
    def print_short_description(word, short_text):
        print()
        print('{:^100}'.format(colored(word, 'cyan', attrs=['bold'])))
        print(colored(' * SHORT DESCRIPTION : ', 'white', attrs=['bold']))
        print(colored('  ---> %s \n' % short_text, 'white'))

    @staticmethod
    def print_long_description(long_text):
        print(colored(' * LONG DESCRIPTION : ', 'grey', attrs=['bold']))
        print(colored('  ---> %s ' % long_text, 'grey'))

    @staticmethod
    def write_dict():
        script_dir = os.path.dirname(__file__)
        voca_path = os.path.join(script_dir, 'vocaDict.py')
        tmp = open(voca_path, 'w')
        tmp.write('vocaDict = %s' % str(vocaDict))
        tmp.close()