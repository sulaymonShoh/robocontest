w = input()
words = []
c = 0
vowels = ['a', 'e', 'i', 'o', 'u']
for i in range(1, len(w) + 1):
    words.append(w[:i])
for i in w:
    if i in vowels: c += 1

print(words[c-1])