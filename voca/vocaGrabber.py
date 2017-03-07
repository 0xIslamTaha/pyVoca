import random
from voca.vocaDict import vocaDict
from voca.vocaUtil import vocaUtil


class vocaGrabber(vocaUtil):
    def __init__(self):
        self.grabber = set()

    def grab_random_words(self, REVISION_NUMBER):
        words = list(vocaDict.keys())

        if REVISION_NUMBER > len(words):
            REVISION_NUMBER = len(words)

        for _ in range(REVISION_NUMBER+1):
            self.grabber.add(words[random.randint(0, REVISION_NUMBER)])

        for key in self.grabber:
            short, long, sentences = self.check_word_in_local_dect(key)
            self.print_driver(key, short, long, sentences)
