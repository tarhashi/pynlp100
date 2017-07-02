def cipher(s):
    return ''.join([chr(219-ord(c)) if c.islower() else c for c in s])

s = "I have a pen."

print(cipher(s))
print(cipher(cipher(s)))