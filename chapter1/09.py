import random
s = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."

def typoglycemia(s):
    ret = [word if len(word) < 4
           else word[0] + ''.join(random.sample(word[1:-1], len(word)-2)) + word[-1]
           for word in s.split()]
    return ' '.join(ret)

print(typoglycemia(s))