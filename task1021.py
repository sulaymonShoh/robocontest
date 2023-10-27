keys = {'w': 'q', 'e': 'w', 'r': 'e', 't': 'r', 'y': 't', 'u': 'y', 'i': 'u', 'o': 'i', 'p': 'o',
        'q': 'p', 's': 'a', 'd': 's', 'f': 'd', 'g': 'f', 'h': 'g', 'j': 'h', 'k': 'j', 'l': 'k',
        'a': 'l', 'x': 'z', 'c': 'x', 'v': 'c', 'b': 'v', 'n': 'b', 'm': 'n', 'z': 'm'}

with open('input.txt', 'r') as fin:
    n = fin.readline()
    text = fin.readline()

res = ''
for i in text:
    res += keys[i]

with open('output.txt', 'w') as fout:
    fout.write(res)