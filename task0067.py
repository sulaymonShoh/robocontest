n = int(input())
bin_n = bin(n)[2:]
if n >= 0:
    res = f'{(32-len(bin_n))*"0"}{bin_n}'
else:
    res = f'{(33-len(bin_n))*"1"}{bin_n[1:]}'
print(res)
# not finished
