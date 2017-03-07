import argparse
from voca.vocaCreator import vocaCreator
from voca.vocaGrabber import vocaGrabber

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', help='search for a list of new words', dest='search', default=[], action='store', nargs='+')
    parser.add_argument('-r', help='revision random n words', dest='revision', default=10, action='store', type=int)
    options = parser.parse_args()

    SEARCH_LIST = options.search
    REVISION_NUMBER = options.revision

    vocaCreator().looking_for_list(SEARCH_LIST)
    vocaGrabber().grab_random_words(REVISION_NUMBER)

