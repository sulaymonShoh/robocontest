h, m = map(int, input().split(':'))
time = int(input())
def add_time(hours, mins, time):
    mins += time
    if mins >= 60:
        hours += mins//60
        mins %= 60
    if hours >= 24:hours %= 24
    return f"{str(hours).zfill(2)}:{str(mins).zfill(2)}"
print(add_time(h, m, time))
#done
