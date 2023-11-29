timezones = {
    "Toshkent": 0,
    "Andijon": -12,
    "Angren": -3,
    "Namangan": -9,
    "Farg'ona": -10,
    "Sirdaryo": 3,
    "Jizzax": 7,
    "Samarqand": 10,
    "Surxondaryo": 11,
    "Qashqadaryo": 14,
    "Navoiy": 17,
    "Buxoro": 20,
    "Xorazm": 35,
    "Qoraqalpog'iston": 36,
}


def time_diff(c1, hh, mm, c2):
    n_hh = hh
    n_mm = mm - timezones[c1] + timezones[c2]

    if n_mm < 0:
        n_mm += 60
        n_hh -= 1
    elif n_mm >= 60:
        n_mm //= 60
        n_hh += 1
    return f"{str(n_hh).zfill(2)}:{str(n_mm).zfill(2)}"


city1 = input()
hh, mm = map(int, input().split(":"))
city2 = input()

print(time_diff(city1, hh, mm, city2))
