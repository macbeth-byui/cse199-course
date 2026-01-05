import sqlite3

# Connect to the database
connection = None
cursor = None

# Create the table if it doesn't already exist



choice = None
while choice != "4":
    print()
    print("1) Add Grade")
    print("2) Show all Grades")
    print("3) Filter Grades by Class")
    print("4) Exit")
    choice = input("> ")

    if choice == "1":
        name = input("Name: ")
        course = input("Course: ")
        grade = float(input("Grade: "))
        # Insert row into the table
        

    elif choice == "2":
        # Query all rows from the table
        

        rows = []
        print(rows)
    elif choice == "3":
        filter = input("Course Filter: ")
        # Query all rows that match the course filter
        

        rows = []
        print("Results: ")
        print(f"{'Name':<10} {'Grade':>6}")
        print("-" * 18)
        for name, grade in rows:
            print(f"{name:<10} {grade:>6.1f}")

connection.close()
