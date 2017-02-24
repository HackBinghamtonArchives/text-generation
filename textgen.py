from collections import defaultdict as dd
import random
from parse import parse

class Hat():
    def __init__(self):
        self.data = []

    def train(self, text):
        for word in parse(text):
            self.data.append(word.lower())

    def gen_sentence(self, n):
        num, words = 0, []
        while num < n:
            words.append(random.choice(self.data))
            num += 1
        words[0] = words[0].title()
        return ' '.join(words)

class Generator():
    def __init__(self):
        self.data = dd(list)

    def train(self, text):
        words = parse(text)

        prev =  words[0]
        words = words[1:]

        for word in words:
            self.data[prev].append(word)
            prev = word

    def gen_sentence(self, n):
        while True:
            num, words = 1, []
            prev = random.choice(list(self.data.keys()))
            words.append(prev)
            while num < n:
                word = random.choice(self.data[prev])
                words.append(word)
                prev = word
                num += 1
            if prev[-1] in '?!.':
                break

        words[0] = words[0].title()
        return ' '.join(words)
