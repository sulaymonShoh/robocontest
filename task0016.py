number = int(input())
list_number = list(str(number))

on = ['', 'o\'n', 'yigirma', 'o\'ttiz', 'qirq', 'ellik', 'oltmish', 'yetmish', 'sakson', 'to\'qson']
bir = ['', 'bir', 'ikki', 'uch', 'to\'rt', 'besh', 'olti', 'yetti', 'sakkiz', 'to\'qqiz']

yuz='yuz'
if len(list_number) > 3 and list_number[-3] == '0': yuz = ''

if number == 0: print('nol')
elif number <= 9: print(f'{bir[number]}')
elif number <= 99: print(f'{on[int(list_number[0])]} {bir[int(list_number[1])]}')
elif number <= 999: print(f'{bir[int(list_number[0])]} {yuz} {on[int(list_number[1])]} {bir[int(list_number[2])]}')
elif number <= 9999: print(f'{bir[int(list_number[0])]} ming {bir[int(list_number[1])]} {yuz} {on[int(list_number[2])]} {bir[int(list_number[3])]}')
elif number <= 99999: print(f'{on[int(list_number[0])]} {bir[int(list_number[1])]} ming {bir[int(list_number[2])]} {yuz} {on[int(list_number[3])]} {bir[int(list_number[4])]}')
elif number <= 999999: print(f'{bir[int(list_number[0])]} {yuz} {on[int(list_number[1])]} {bir[int(list_number[2])]} ming {bir[int(list_number[3])]} {yuz} {on[int(list_number[4])]} {bir[int(list_number[5])]}')
elif number <= 9999999: print(f'{bir[int(list_number[0])]} million {bir[int(list_number[1])]} yuz {on[int(list_number[2])]} {bir[int(list_number[3])]} ming {bir[int(list_number[4])]} {yuz} {on[int(list_number[5])]} {bir[int(list_number[6])]}')
elif number <= 99999999: print(f'{on[int(list_number[0])]} {bir[int(list_number[1])]} million {bir[int(list_number[2])]} {yuz} {on[int(list_number[3])]} {bir[int(list_number[4])]} ming {bir[int(list_number[5])]} {yuz} {on[int(list_number[6])]} {bir[int(list_number[7])]}')
elif number <= 999999999: print(f'{bir[int(list_number[0])]} {yuz} {on[int(list_number[1])]} {bir[int(list_number[2])]} million {bir[int(list_number[3])]} {yuz} {on[int(list_number[4])]} {bir[int(list_number[5])]} ming {bir[int(list_number[6])]} {yuz} {on[int(list_number[7])]} {bir[int(list_number[8])]}')
elif number <= 9999999999: print(f'{bir[int(list_number[0])]} milliard {bir[int(list_number[1])]} {yuz} {on[int(list_number[2])]} {bir[int(list_number[3])]} million {bir[int(list_number[4])]} {yuz} {on[int(list_number[5])]} {bir[int(list_number[6])]} ming {bir[int(list_number[7])]} {yuz} {on[int(list_number[8])]} {bir[int(list_number[9])]}')
elif number <= 99999999999: print(f'{on[int(list_number[0])]} {bir[int(list_number[1])]} milliard {bir[int(list_number[2])]} {yuz} {on[int(list_number[3])]} {bir[int(list_number[4])]} million {bir[int(list_number[5])]} {yuz} {on[int(list_number[6])]} {bir[int(list_number[7])]} ming {bir[int(list_number[8])]} {yuz} {on[int(list_number[9])]} {bir[int(list_number[10])]}')