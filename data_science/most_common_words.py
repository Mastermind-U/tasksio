import sys
from collections import Counter
from multiprocessing import Pool
# import nltk
# from nltk.corpus import stopwords
# nltk.download("stopwords")

# stop_words = stopwords.words()

try:
    num_words = int(sys.argv[1])
except Exception:
    print("Применение: most_common_words.py num_words")
    sys.exit(1)  # код 1 - error


def get_words(word):
    if word:
        return word.lower()


with Pool(100) as p:
    counter = Counter(p.map(get_words, [word for line in sys.stdin for word in line.strip().split()]))

for word, count in counter.most_common(num_words):
    sys.stdout.write(str(count))
    sys.stdout.write("\t")
    sys.stdout.write(word)
    sys.stdout.write("\n")
