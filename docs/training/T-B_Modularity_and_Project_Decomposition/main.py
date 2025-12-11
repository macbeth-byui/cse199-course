# CSE 199 - Training B

# Import the functions defined in other files that we want to call

from conversions import convert_cups
from conversions import convert_tbsp
from conversions import convert_tsp

def show_menu():
    '''
    Display a menu for the user, call the proper conversion,
    and display the results
    '''
    choice = None
    while choice != "4":
        print("1) Convert cups")
        print("2) Convert tablespoons")
        print("3) Convert teaspoons")
        print("4) Quit")
        choice = input("> ")
        if choice == "1":
            cups = float(input("Enter the number of cups: "))
            result = convert_cups(cups)
            display_result(result)
        elif choice == "2":
            tbsp = float(input("Enter the number of tablespoons: "))
            result = convert_tbsp(tbsp)
            display_result(result)
        elif choice == "3":
            tsp = float(input("Enter the number of teaspoons: "))
            result = convert_tsp(tsp)
            display_result(result)

def display_result(result):
    '''
    Display the result.  The result is expected to be in the 
    format of (cups, tablespoons, teaspoons).
    '''
    print(f"Cups: {result[0]:.2f} Tablespoons: {result[1]:.2f} Teaspoons: {result[2]:.2f}")


# Show the menu to start the programming.  Note, it is common
# practice in python to use a main function here.
show_menu()