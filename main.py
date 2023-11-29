"""
Optional homework – implementation operations + conversions  

share in the final grade: 10%  
deadline for homework submission: 10.12.2023, 10pm. 

The application must implement algorithms for:  
- arithmetic operations for positive integers: addition, subtraction, multiplication and division by one digit, in a base pÎ{2,3,...,9,10,16} 
- conversions of natural numbers between two bases p,qÎ{2,3,...,9,10,16} using the substitution method or successive divisions and rapid conversions between two bases p,qÎ{2, 4, 8, 16}. 
and must have a menu such that all operations and conversion methods to be verified separately. 
The executable form, the code of the application and the documentation will be submitted in the corresponding assignment on Teams. The documentation will follow the same structure as the Programming Fundament’s documentations, and it must contain at least: the problem statement for the implemented application, the used algorithms in pseudo-code, implementation considerations and test data.  

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
1p used data type specification 
3p specification and pseudo-code for the important algorithms used (input, output, preconditions, post-conditions -1p; pseudo-code 2p) 
3p at least a set of test data for the complete application, more data sets where is needed 
1p documentation clearness (structured, well written, ...) 

NOTE: If the electronic homework is at least 80% similar (http://www.tools4noobs.com/online_tools/string_similarity/) to another one from this year or a previous year of study, the electronic homework will not be corrected (neither the documentation), and the corresponding points are lost.
"""


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


# addition (a, b) in a given base (base)
def add(a, b, base):
    pass


# subtraction (a, b) in a given base (base)
def sub(a, b, base):
    pass


# multiplication (a*b) in a base (base) by 1 digit (d)
def multiply(a, b, base):
    pass


# division (a/b) in a base (base) by 1 digit (b)
def divide(a, b, base):
    pass


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
while True:
    option = int(input("\nEnter an option from the menu: "))
    print("")
    if option == 1:
        print("opt1")

    elif option == 2:
        print("opt2")

    elif option == 3:
        print("opt3")

    elif option == 4:
        print("opt4")

    elif option == 5:
        print("opt5")

    elif option == 6:
        print("opt6")

    elif option == 7:
        print("opt6")

    elif option == 8:
        print("opt6")

    elif option == 9:
        print("You exited the program, thank you!")
        exit()
    else:
        print("Invalid option, please enter a number between 1 and 9.")
