def print_menu():
    menu_options = {
        1: "Read a list of complex numbers from the console",
        2: "Display the entire list of numbers to the console",
        3: "Display the length and elements of a longest subarray of numbers that contain at most 3 distinct values and"
        " print the length and elements \n    of a maximum subarray sum, when considering each number's real part",
        4: "Exit the program",
    }
    for key in menu_options.keys():
        print(key, "~", menu_options[key])
