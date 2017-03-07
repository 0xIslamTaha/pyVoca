from termcolor import colored
from voca.vocaDict import vocaDict


class vocaUtil():

    def check_word_in_local_dect(self, word):
        if word in vocaDict:
            return vocaDict[word]['short'], vocaDict[word]['long'], vocaDict[word]['sentences']
        else:
            return None, None, None

    def print_driver(self, word, short_text, long_text, sentences):
        self.print_short_description(word, short_text)
        self.print_long_description(long_text)
        self.print_sentences(sentences)

    def print_short_description(self, word, short_text):
        print()
        print('{:^100}'.format(colored(word, 'cyan', attrs=['bold'])))
        print(colored(' * SHORT DESCRIPTION : ', 'yellow', attrs=['bold']))
        print(colored('  ---> %s \n' % short_text, 'yellow'))

    def print_long_description(self, long_text):
        print(colored(' * LONG DESCRIPTION : ', 'green', attrs=['bold']))
        print(colored('  ---> %s \n' % long_text, 'green'))
        print(colored(' * SENTENCE EXAMPLES : ', 'white', attrs=['bold']))

    def print_sentences(self, sentences):
        if sentences:
            for sentence in sentences:
                print(colored('  ---> %s ' % sentence, 'white'))
