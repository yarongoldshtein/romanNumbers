def int_to_roman(num):
    numbers = [1000000, 900000, 500000, 400000, 100000, 90000, 50000, 40000, 10000, 9000, 5000, 4000, 1000, 900, 500,
               400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    romans = ["^M", "^C^M", "^D", "^C^D", "^C", "^X^C", "^L", "^X^L", "^X", "^I^X", "^V", "M^V", "M", "CM", "D",
              "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    roman_num = ""
    i = 0
    while num > 0:
        while (num // numbers[i]) > 0:
            roman_num += romans[i]
            num -= numbers[i]
        i += 1
    return roman_num


def is_float(value):
    try:
        float(value)
        return True
    except ValueError:
        return False


def check_for_zero(num):
    if int(num) == 0:
        print("N")
    else:
        print(int_to_roman(int(num)))


def is_valid(num):
    if num.isdigit():
        if int(num) > 3999999:
            return False
        else:
            return True


flag = True
while flag:
    num = input("Enter an Integer between 0 and 3,999,999: ").strip()
    while not is_valid(num):
        print("Invalid input, please enter a positive integer!\n")
        num = input("Enter an Integer between 0 and 3,999,999: ").strip()
    else:
        check_for_zero(num)
    yes_or_no = input("Again? ")
    if yes_or_no.lower() == "n":
        flag = False
