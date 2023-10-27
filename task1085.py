def decode(code):
    res = ''
    while len(code)//2>=1:
        char = code[:2]
        code = code[2:]
        if int(char) < 65:
            char += code[0]
            code = code[1:]
        res += chr(int(char))
    return res

print(decode(input()))
