def translate(number):
    on = [
        "",
        "o'n",
        "yigirma",
        "o'ttiz",
        "qirq",
        "ellik",
        "oltmish",
        "yetmish",
        "sakson",
        "to'qson",
    ]
    bir = [
        "",
        "bir",
        "ikki",
        "uch",
        "to'rt",
        "besh",
        "olti",
        "yetti",
        "sakkiz",
        "to'qqiz",
    ]
    list_number = list(str(number))

    if number.isdigit():
        number = int(number)
        if len(list_number) > 3 and list_number[-3] == "0":
            yuz = ""
        else:
            yuz = "yuz"

        if number == 0:
            return "nol"
        elif number <= 9:
            return f"{bir[number]}"
        elif number <= 99:
            return f"{on[int(list_number[0])]} {bir[int(list_number[1])]}"
        elif number <= 999:
            return f"{bir[int(list_number[0])]} yuz {on[int(list_number[1])]} {bir[int(list_number[2])]}"
        elif number <= 9999:
            return f"{bir[int(list_number[0])]} ming {bir[int(list_number[1])]} {yuz} {on[int(list_number[2])]} {bir[int(list_number[3])]}"
        elif number <= 99999:
            return f"{on[int(list_number[0])]} {bir[int(list_number[1])]} ming {bir[int(list_number[2])]} {yuz} {on[int(list_number[3])]} {bir[int(list_number[4])]}"
        elif number <= 999999:
            return f"{bir[int(list_number[0])]} yuz {on[int(list_number[1])]} {bir[int(list_number[2])]} ming {bir[int(list_number[3])]} {yuz} {on[int(list_number[4])]} {bir[int(list_number[5])]}"
        elif number <= 9999999:
            return f"{bir[int(list_number[0])]} million {bir[int(list_number[1])]} yuz {on[int(list_number[2])]} {bir[int(list_number[3])]} ming {bir[int(list_number[4])]} {yuz} {on[int(list_number[5])]} {bir[int(list_number[6])]}"
        elif number <= 99999999:
            return f"{on[int(list_number[0])]} {bir[int(list_number[1])]} million {bir[int(list_number[2])]} yuz {on[int(list_number[3])]} {bir[int(list_number[4])]} ming {bir[int(list_number[5])]} {yuz} {on[int(list_number[6])]} {bir[int(list_number[7])]}"
        elif number <= 999999999:
            return f"{bir[int(list_number[0])]} yuz {on[int(list_number[1])]} {bir[int(list_number[2])]} million {bir[int(list_number[3])]} yuz {on[int(list_number[4])]} {bir[int(list_number[5])]} ming {bir[int(list_number[6])]} {yuz} {on[int(list_number[7])]} {bir[int(list_number[8])]}"
        elif number <= 9999999999:
            return f"{bir[int(list_number[0])]} milliard {bir[int(list_number[1])]} yuz {on[int(list_number[2])]} {bir[int(list_number[3])]} million {bir[int(list_number[4])]} yuz {on[int(list_number[5])]} {bir[int(list_number[6])]} ming {bir[int(list_number[7])]} {yuz} {on[int(list_number[8])]} {bir[int(list_number[9])]}"
        elif number <= 99999999999:
            return f"{on[int(list_number[0])]} {bir[int(list_number[1])]} milliard {bir[int(list_number[2])]} yuz {on[int(list_number[3])]} {bir[int(list_number[4])]} million {bir[int(list_number[5])]} yuz {on[int(list_number[6])]} {bir[int(list_number[7])]} ming {bir[int(list_number[8])]} {yuz} {on[int(list_number[9])]} {bir[int(list_number[10])]}"

    # else: print('Faqat sonlarni kiriting!!!')


print(translate(input()).replace("  ", " ").replace("  ", " "))
