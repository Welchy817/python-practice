# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import Counter

N = int(input())
words = []
for i in range(N):
    words.append(input())

word_count = Counter(words)
print(len(word_count))
print(' '.join(map(str, word_count.values())))