s = "I am an NLPer"
words = s.split()

def ngram(seq, n):
    return [seq[i:i+n] for i in range(0, len(seq) - n + 1)]

print(ngram(s, 2))
print(ngram(words, 2))