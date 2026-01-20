text = "Simple code is better than complex code, but simple code is hard."

print(text.count(','))
print(text.replace(',', ''))

words = text.lower().split()
print(words)

count_words = {}
for word in words:
    count_words[word] = count_words.get(word, 0) + 1
print(count_words)
new = {k:w for k, w in count_words.items() if w > 1}
print(new)

sorted_w = dict(sorted(count_words.items(), key=lambda item: item[1], reverse=True))
print(sorted_w)