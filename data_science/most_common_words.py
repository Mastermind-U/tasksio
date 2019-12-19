import sys
from collections import Counter
from tqdm import tqdm

try:
    num_words = int(sys.argv[1])
except Exception:
    print("Применение: most_common_words.py num_words")
    sys.exit(1)  # код 1 - error

counter = Counter(
    word.lower()
    for line in sys.stdin
    for word in line.strip().split()
    if word
)

for word, count in counter.most_common(num_words):
    sys.stdout.write(str(count))
    sys.stdout.write("\t")
    sys.stdout.write(word)
    sys.stdout.write("\n")
