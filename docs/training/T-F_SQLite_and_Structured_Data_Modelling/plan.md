# Training F - SQLite & Structured Data Modelling

## Background

* Databases are a great way to store, modify, and search large amounts of data in your software.

* There are databases based on SQL (Structured Query Language) and Key-Value databases.  JSON is a simple example of a Key-Value database.

* SQL databases work with tables of information.  Each row represents one entry and each column represents one attribute for each entry.  Consider the example table below that represents grades:

|grade_id  |name       |class      |grade  |
|:--------:|-----------|-----------|-------|
| 1        | Bob       | CSE 210   | 95    |
| 2        | Tim       | CSE 210   | 84.2  |
| 3        | Sue       | CSE 212   | 92.3  |

* We can create and use this table using SQL commands:

|Action         | SQL Command                                                                                                        |
|---------------|--------------------------------------------------------------------------------------------------------------------|
|Create Database| `CREATE TABLE IF NOT EXISTS Grades (grade_id INT PRIMARY KEY AUTOINCREMENT, name TEXT, course TEXT, grade FLOAT);` |
|Insert Row     | `INSERT INTO Grades (name, course, grade) VALUES ('Bob', 'CSE 210', 95);`                                          |
|Delete Row     | `DELETE FROM Grades WHERE grade_id = 2;`                                                                           |
|Update Row     | `UPDATE Grades SET grade = 93 WHERE grade_id = 3;`                                                                 |
|Query All Rows | `SELECT * FROM Grades;`                                                                                            |
|Query CSE 210  | `SELECT name, grade FROM Grades WHERE course = 'CSE 210';`                                                         |

* Python has native support for SQLite.  No installations are needed.  The database is stored in a file with your Python code.

|Action                 | Python Command                                       |
|-----------------------|------------------------------------------------------|
|Open or Create Database| `connection = sqlite3.connect("grades.db")`          |
|Get the DB `cursor`    | `cursor = connection.cursor()`                       |
|Run SQL Command        | `cursor.execute("SQL Command ? ?", (Value1, Value2))`|
|Get Results from Query | `rows = cursor.fetchall()`                           |
|Commit Changes to DB   | `connection.commit()`                                |
|Close Database         | `connection.close()`                                 |

## Example

1. Copy the following code into a file called `main.py`:

```python
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
```

1. Connect to a database called `grades.db` and establish the cursor.

1. Create the `Grades` table as described in the reading above.

1. Insert grade entries into the table based on the user input.

1. Display all data in the table.

1. Display all data for a user supplied course.

1. Exit the program and restart to verify that the data is preserved in the database.

## Discussion

How could a database be used in your project?  How are databases perhaps better than storing data in text files?

## Solution

* [main.py](main.py)
