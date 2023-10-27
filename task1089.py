n = int(input())
b = ['', 'bir', 'ikki', 'uch', 'to\'rt', 'besh', 'olti', 'yetti', 'sakkiz', 'to\'qqiz']
o = ['', 'o\'n', 'yigirma', 'o\'ttiz', 'qirq', 'ellik', 'oltmish', 'yetmish', 'sakson', 'to\'qson']
lstn = list(str(n))


def naturalson(num):
    if num <= 9:
        return b[num]
    elif num <= 99:
        return f'{o[int(lstn[0])]} {b[int(lstn[1])]}'.strip()
    elif num <= 999:
        return f'{b[int(lstn[0])]} yuz {o[int(lstn[1])]} {b[int(lstn[2])]}'.strip()
    else:
        return 'bir ming'


print(naturalson(n))
