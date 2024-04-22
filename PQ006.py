#Write a python program to convert decimal to hexadecimal.


def dectohex(n):
    if n < 10:
        return str(n)
    elif n == 10:
        return 'A'
    elif n == 11:
        return 'B'
    elif n == 12:
        return 'C'
    elif n == 13:
        return 'D'
    elif n == 14:
        return 'E'
    elif n == 15:
        return 'F'
    else:
        return dectohex(n // 16) + dectohex(n % 16)

decimal_nums = [0, 15, 30, 55, 355, 656, 896, 1125]

print("Decimal numbers:")
print(decimal_nums)

print("\nHexadecimal numbers of the said decimal numbers:")
print([dectohex(x) for x in decimal_nums])
