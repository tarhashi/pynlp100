str = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."

words = str.replace(',', '').replace('.', '').split()
word_lengthes = [len(word) for word in words]
print(word_lengthes)