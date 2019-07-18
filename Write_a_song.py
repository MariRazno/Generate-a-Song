from nltk.util import bigrams
from nltk import FreqDist
from nltk.tokenize import word_tokenize
import random

def n_grams(word):
    bigrams_text = []
    with open(r"C:\PyCharmGrammarly\Grammarly\lyrics.txt", 'r') as tok:
        raw_text = tok.read()
        raw_text = raw_text.split("\n")
        lines = []
        for i in raw_text:
            tokens = word_tokenize(i)
            lines.append(tokens)
        for l in lines:
            b = list(bigrams(l))
            bigrams_text.extend(b)
        k = 0
        song = []
        selection = []
        while k <= 96:
            k = k + 1
            for first in bigrams_text:
                if word == first[0]:
                    selection.append(first)
            freq_bi = FreqDist(selection)
            best = freq_bi.most_common()
            word = random.choice(best)
            word = word[0][1]
            song.append(word)
        words_in_line = 0
        for lyric in song:
            words_in_line +=1
            if words_in_line % 5 == 0:
                print(lyric, "\n")
                continue
            else:
                print(lyric, end=" ")


n_grams("ooh")

