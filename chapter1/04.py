s = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
words = s.split()

def head_length(index):
    firsts = [1, 5, 6, 7, 8, 9, 15, 16, 19]
    if index + 1 in firsts:
        return 1
    else:
        return 2

dic = dict([(word[:head_length(idx)], idx + 1) for idx, word in enumerate(words)])
print(dic)