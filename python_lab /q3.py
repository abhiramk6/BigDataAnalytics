import sys

dict = {}

for line in sys.stdin:

    line = line.strip()

    line = line.split()

    for word in line:
        t = dict.get(word, 0)
        dict[word] = t + 1

print(dict)
