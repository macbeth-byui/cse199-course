import sqlite3

# Connect to the database
connection = sqlite3.connect("grades.db")
cursor = connection.cursor()

# Create the table if it doesn't already exist
cursor.execute("CREATE TABLE IF NOT EXISTS Grades (grade_id INT PRIMARY KEY AUTOINCREMENT, name TEXT, course TEXT, grade FLOAT)")
connection.commit()

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
        cursor.execute("INSERT INTO Grades (name, course, grade) VALUES (?, ?, ?)", (name, course, grade))
        connection.commit()
    elif choice == "2":
        # Query all rows from the table
        cursor.execute("SELECT * FROM Grades")
        rows = cursor.fetchall()
        print(rows)
    elif choice == "3":
        filter = input("Course Filter: ")
        # Query all rows that match the course filter
        cursor.execute("SELECT name, grade FROM Grades WHERE course = ?", (filter,))
        rows = cursor.fetchall()
        print("Results: ")
        print(f"{'Name':<10} {'Grade':>6}")
        print("-" * 18)
        for name, grade in rows:
            print(f"{name:<10} {grade:>6.1f}")

connection.close()
