roman_map = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}


def roman_to_int(str):
    ans = 0
    for i in range(len(str)):
        if i > 0 and roman_map[str[i]] > roman_map[str[i - 1]]:
            ans += roman_map[str[i]] - 2 * roman_map[str[i - 1]]
        else:
            ans += roman_map[str[i]]
    return ans


def is_valid(str):
    if set(roman).issubset("IVXLCDM"):
        if set(roman).issubset("^"):
            return False
        for j in range(len(str)):
            if j > 1 and roman_map[str[j]] > roman_map[str[j - 1]] >= roman_map[str[j - 2]]:
                return False
            if j > 1 and roman_map[str[j]] == roman_map[str[j - 1]] and roman_map[str[j]] > roman_map[str[j - 2]]:
                return False
            if j > 1 and roman_map[str[j]] < roman_map[str[j - 1]] and roman_map[str[j]] == roman_map[str[j - 2]]:
                return False
            if j > 2 and roman_map[str[j]] == roman_map[str[j - 1]] == roman_map[str[j - 2]] == roman_map[str[j - 3]]:
                return False
        return True
    else:
        return False


def check_for_zero(str):
    if str == "N":
        print(0)
    else:
        print(roman_to_int(str))


flag = True
while flag:
    roman = input("Enter a roman number: ").strip()
    while not is_valid(roman):
        print("Invalid input, please enter a valid roman number!\n")
        roman = input("Enter an roman number: ").strip()
    else:
        check_for_zero(roman)
    yes_or_no = input("Again? ")
    if yes_or_no.lower() == "n":
        flag = False
