"""
Optional homework – implementation operations + conversions  

share in the final grade: 10%  
deadline for homework submission: 10.12.2023, 10pm. 

The application must implement algorithms for:  
- arithmetic operations for positive integers: addition, subtraction, multiplication and division by one digit, in a base pÎ{2,3,...,9,10,16} 
- conversions of natural numbers between two bases p,qÎ{2,3,...,9,10,16} using the substitution method or successive divisions and rapid conversions between two bases p,qÎ{2, 4, 8, 16}. 
and must have a menu such that all operations and conversion methods to be verified separately. 
The executable form, the code of the application and the documentation will be submitted in the corresponding assignment on Teams. The documentation will follow the same structure as the Programming Fundment’s documentations, and it must contain at least: the problem statement for the implemented application, the used algorithms in pseudo-code, implementation considerations and test dta.  

The grade is computed as follows: 
10%: by default 
70% : the application (the authors name will be found in code and will be visible at run time too) 
1p - algorithm for the method of successive divisions  
1p - algorithm for the substitution method  
1p – algorithm for conversion using 10 as an intermediate base 
2p - rapid conversions (executable form) between two bases p,qÎ{2, 4, 8, 16}. 
1p addition of two numbers in a base 
1p subtraction of two numbers in a base 
1p multiplication of a number by a digit in a base 
1p division of a number by a digit in a base 
1p code quality (indentation, use of comments, suggestive variables names) 
20%: documentation  
1p problem statement 
1p sub-algorithm’s diagram 
1p used dta type specification 
3p specification and pseudo-code for the important algorithms used (input, output, preconditions, post-conditions -1p; pseudo-code 2p) 
3p at least a set of test dta for the complete application, more dta sets where is needed 
1p documentation clearness (structured, well written, ...) 

NOTE: If the electronic homework is at least 80% similar (http://www.tools4noobs.com/online_tools/string_similarity/) to another one from this year or a previous year of study, the electronic homework will not be corrected (neither the documentation), and the corresponding points are lost.
"""

import os


def print_menu():
    menu_options = {
        1: "Read a list of complex numbers from the console",
        2: "Display the entire list of numbers to the console",
        3: "Display the length and elements of a longest subarray of numbers that contain at most 3 distinct values and"
        " print the length and elements \n    of a maximum subarray sum, when considering each number's real part",
        4: "ceva",
        5: "ceva",
        6: "ceva",
        7: "Exit the program",
    }
    for key in menu_options.keys():
        print(key, "~", menu_options[key])


def getLastCharDumb(n: str) -> int:
    if n[-1] == "A":
        return 10
    if n[-1] == "B":
        return 11
    if n[-1] == "C":
        return 12
    if n[-1] == "D":
        return 13
    if n[-1] == "E":
        return 14
    if n[-1] == "F":
        return 15
    if n[-1] > "0" and n[-1] < "9":
        return int(n[-1])


def getLastCharSmart(n: str) -> int:
    """
    Converts the last character of a given string n to an integer, treating the character as a hexadecimal digit.

    Args:
        n (str): The input string.

    Returns:
        int: The integer representation of the last character.

    """
    return int(n[-1], 16)


def getFirstTwoChars(n: str) -> int:
    return int(t2s(n[:2]), 16)


def getFirstChar(n: str) -> int:
    return int(n[0], 16)


def toHex(
    n: int,
) -> str:  # n in [0, 15], takes a number and returns its hex representation
    """
    Converts a number to its hexadecimal representation.

    Args:
        n (int): The number to be converted. Must be in the range [0, 15].

    Returns:
        str: The hexadecimal representation of the number.
    """
    if n < 10:
        return str(n)
    char_in_unicode = (
        n + 55
    )  # ? 55 = ord('A') - 10 -- ord('A') = 65; representing the character in unicode
    return chr(char_in_unicode)


def to_decimal(num, base):
    res, power = 0, 1
    while num > 0:
        digit = num % 10
        res += digit * power
        power *= base
        num //= 10
    return res


def to_base(num, base):
    res, power = 0, 1
    while num > 0:
        digit = num % base
        res += digit * power
        power *= 10
        num //= base
    return res


def t2s(t: tuple) -> str:
    """
    Converts a tuple of integers to a string.

    Args:
        t (tuple): The tuple to be converted.

    Returns:
        str: The string representation of the tuple.
    """
    s = ""
    for elem in t:
        s += str(elem)
    return s


# addition (a, b) in a given base (base)
def add(a: str, b: str, base: int) -> str:
    _sum = 0
    if base <= 10:
        a = int(a)
        b = int(b)
        _sum = 0
        carry = 0
        p = 1

        maxx = max(len(str(a)), len(str(b)))

        for _ in range(1, maxx + 1):
            digit_sum = a % 10 + b % 10 + carry
            _sum += (digit_sum % base) * p
            carry = digit_sum // base
            a //= 10
            b //= 10
            p *= 10

        if carry > 0:
            _sum += carry * p

        _sum = str(_sum)
    elif base == 16:
        _sum = ""
        carry = 0

        maxx = max(len(a), len(b))

        while len(a) != len(b):
            if len(a) < len(b):
                a = "0" + a
            else:
                b = "0" + b

        for _ in range(0, maxx):
            digit_sum = getLastCharSmart(a) + getLastCharSmart(b) + carry
            if digit_sum >= 16:
                _sum = toHex(digit_sum - 16) + _sum
                carry = 1
            else:
                _sum = toHex(digit_sum) + _sum
                carry = 0
            a = a[:-1]
            b = b[:-1]

        if carry > 0:
            s = str(carry) + _sum[0]
            _sum = toHex(getLastCharSmart(s)) + _sum[1:]

    return _sum


# subtraction (a, b) in a given base (base)
def sub(a, b, base):
    if base <= 10:
        a = int(a)
        b = int(b)

        finalVal = 0
        carry = 0
        power = 1

        while a > 0:
            d = a % 10
            db = b % 10

            a = a // 10
            b = b // 10

            aux = d - db + carry

            if aux < 0:
                carry = -1  # acts as borrow
                aux += base

            else:
                carry = 0

            # Add in final result
            finalVal += aux * power
            power = power * 10
    elif base == 16:
        finalVal = ""
        carry = 0

        maxx = max(len(a), len(b))

        while len(a) != len(b):
            if len(a) < len(b):
                a = "0" + a
            else:
                b = "0" + b

        for _ in range(0, maxx):
            digit_sub = getLastCharSmart(a) - getLastCharSmart(b) + carry
            if digit_sub < 0:
                finalVal = toHex(digit_sub + 16) + finalVal
                carry = -1
            else:
                finalVal = toHex(digit_sub) + finalVal
                carry = 0
            a = a[:-1]
            b = b[:-1]

    return finalVal


# multiplication (a*b) in a base (base) by 1 digit (b)
def multiply_1_digit(a, b, base):
    if base <= 10:
        a = int(a)
        b = int(b)

        finalValue = 0
        carry = 0
        power = 1

        while a > 0:
            d = a % 10
            m = (d * b) + carry
            finalValue += (m % base) * power
            carry = m // base
            a = a // 10
            power = power * 10

        if carry > 0:
            finalValue += carry * power
    elif base == 16:
        finalValue = ""
        carry = 0

        maxx = max(len(a), len(b))

        # while len(a) != len(b):
        #     if len(a) < len(b):
        #         a = "0" + a
        #     else:
        #         b = "0" + b

        for _ in range(0, maxx):
            digit_prod = getLastCharSmart(a) * getLastCharSmart(b) + carry
            finalValue = toHex(digit_prod % 16) + finalValue
            carry = digit_prod // 16
            a = a[:-1]
            # b = b[:-1]

        if carry > 0:
            finalValue = toHex(carry) + finalValue
    return finalValue


# division (a/b) in a base (base) by 1 digit (b)
def divide_1_digit(a, b, base):
    # divide a number 'a' by a digit 'b' in a given base 'base'
    if base <= 10:
        a = int(a)
        b = int(b)

        finalValue = 0

        while a > b:
            power = 1

            while power * 10 < a:
                power *= 10
            d = a // power

            if d < b:
                power //= 10
                d = a // power

            d = to_decimal(d, base)
            carry = d % b
            finalValue = finalValue * 10 + d // b
            a = carry * power + a % power
    elif base == 16:
        finalValue = ""
        a = a.upper()
        b = b.upper()

        carry = 0

        while int(a) > int(b):
            if int(a[0]) < int(b):
                digit_div = to_decimal(getFirstTwoChars(a), 16) // getLastCharSmart(b)
                finalValue = finalValue + toHex(digit_div)
                carry = getFirstTwoChars(a) % getLastCharSmart(b)
                a = str(carry) + a[2:]
            else:
                digit_div = to_decimal(getFirstChar(a), 16) // getLastCharSmart(b)
                finalValue = finalValue + toHex(digit_div)
                carry = getFirstTwoChars(a) % getLastCharSmart(b)
                a = str(carry) + a[1:]

    return finalValue, a


# successive divisions (from BASE -> base) (@params: n, BASE, base)
def successive_div_conversion(n, BASE, base):
    pass


# substitution method
def substitution_conversion():
    pass


# conversions using 10 as an intermediate base
def simple_conversion():
    pass


# rapid conversions between 2 bases (base in {2, 4, 8 16})
def rapid_conversions():
    pass


# mainu
if __name__ == "__main__":
    while True:
        os.system("cls") if os.name == "nt" else os.system(
            "clear"
        )  # clear screen for windows and linux (dca vrei sa di clear screen in terminal si nu stii ce OS are userul; in cazul tau poti sa lasi doar os.system("clear"))
        option = int(input("\nEnter an option from the menu: "))
        print("")
        if option == 1:
            print("Addition\n")
            base = int(input("Enter a base you want to work with: base = "))
            a = input(f"Enter number in base {base} a= ")
            b = input(f"Enter number in base {base} b= ")
            print(add(a, b, base))
            input("Press any key to continue...")

        elif option == 2:
            print("Substraction\n")
            base = int(input("Enter a base you want to work with: base = "))
            a = input(f"Enter number in base {base} a= ")
            b = input(f"Enter number in base {base} b= ")
            print(sub(a, b, base))
            input("Press any key to continue...")

        elif option == 3:
            print("Multiplication by 1 digit\n")
            base = int(input("Enter a base you want to work with: base = "))
            a = input(f"Enter number in base {base} a= ")
            b = input(f"Enter digit in base {base} b= ")
            print(multiply_1_digit(a, b, base))
            input("Press any key to continue...")

        elif option == 4:
            print("Division by 1 digit\n")
            base = int(input("Enter a base you want to work with: base = "))
            a = input(f"Enter number in base {base} a= ")
            b = input(f"Enter digit in base {base} b= ")
            res = divide_1_digit(a, b, base)
            print(res[0], "remainder", res[1])
            input("Press any key to continue...")

        #     elif option == 5:
        #         print("opt5")

        #     elif option == 6:
        #         print("opt6")

        #     elif option == 7:
        #         print("opt6")

        #     elif option == 8:
        #         print("opt6")

        elif option == 9:
            print("You exited the program, thank you!")
            exit()
        else:
            print("Invalid option, please enter a number between 1 and 9.")
