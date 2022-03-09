sec = int(input())

hrs = sec//3600
sec -= hrs*3600
hrs = hrs%24
mins = sec//60
sec -= mins*60
secs = sec

if mins<10:mins = f'0{mins}'
if secs<10:secs = f'0{secs}'
print(f'{hrs}:{mins}:{secs}')