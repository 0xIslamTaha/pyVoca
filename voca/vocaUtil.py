from termcolor import colored
from voca.vocaDict import vocaDict

class vocaUtil():
    @staticmethod
    def print_short_description(word, short_text):
        print()
        print('{:^100}'.format(colored(word, 'cyan', attrs=['bold'])))
        print(colored(' * SHORT DESCRIPTION : ', 'yellow', attrs=['bold']))
        print(colored('  ---> %s \n' % short_text, 'yellow'))

    @staticmethod
    def print_long_description(long_text):
        print(colored(' * LONG DESCRIPTION : ', 'green', attrs=['bold']))
        print(colored('  ---> %s \n' % long_text, 'green'))
        print(colored(' * SENTENCE EXAMPLES : ', 'white', attrs=['bold']))

    @staticmethod
    def print_sentences(sentences):
        for sentence in sentences:
            print(colored('  ---> %s ' % sentence, 'white'))