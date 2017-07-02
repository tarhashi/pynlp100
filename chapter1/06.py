def ngram(seq, n):
    return [seq[i:i+n] for i in range(0, len(seq) - n + 1)]

bigram1 = ngram("paraparaparadise", 2)
bigram2 = ngram("paragraph", 2)

set1 = set(bigram1)
set2 = set(bigram2)

# 和集合
print(set1|set2)
# 積集合
print(set1&set2)
# 差集合
print(set1-set2)

print('se' in set1)
print('se' in set2)