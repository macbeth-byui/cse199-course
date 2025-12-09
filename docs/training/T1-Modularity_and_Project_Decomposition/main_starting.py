choice = None
while choice != "4":
    print("1) Convert cups")
    print("2) Convert tablespoons")
    print("3) Convert teaspoons")
    print("4) Quit")
    choice = input("> ")
    if choice == "1":
        cups = float(input("Enter the number of cups: "))
    elif choice == "2":
        tbsp = float(input("Enter the number of tablespoons: "))
    elif choice == "3":
        tsp = float(input("Enter the number of teaspoons: "))

