# Training 1 - Modularity and Project Decomposition

## Background

* When solving a problem, break it up into parts.  How will you calculate something?  How will you read information from the user?  How many different scenarios do you need to handle?

* In software, we want to take the individual parts and place them in separate functions and separate files.  Separate functions provide the ability for reuse.

* In Python, if you put a function in a different file, you need to import that function when you call it.  The format is:

    ```python
    from file_name import function_name  # Don't include the .py 
    ```

* Benefits:
  * Reuse functions
  * You can test a single function
  * Implement only part of the software and it still runs
  * Easier to find functions in large code bases
  * Multiple team members can modify different files at the same time

## Example

In this example, we will create a tool to convert measurements in cups, tablespoons, and teaspoons.  Our goal is to implement the following function diagram:

![Function Diagram](function_diagram.drawio.png)

1. Copy the following code into a file called `main.py`:

    ```python
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
    ```

1. Convert the code in `main.py` into a function called `show_menu`.  Call the `show_menu` function.  Run the program.

1. Use modularity to implement the program according to the diagram above.  Create functions `convert_cups`, `convert_tbsp`, and `convert_tsp` into a file `conversions.py`.  Each function should return a tuple `(cups, tbsp, tsp)`.

1. Call the `convert` functions written in `conversions.py`.  Remember to use the `import` statements.  Run the `main.py` program.

1. Create a function called `display_results` that will take the `(cups, tbsp, tsp)` into the format:  `Cups: #.## Tablespoons: #.## Teaspoons: #.##`.  Run the `main.py` program.

## Discussion

How will modularity and problem decomposition affect your personal project this semester?

## Solution

* [main.py](training/T1-Modularity_and_Project_Decomposition/main.py)

* [conversions.py](training/T1-Modularity_and_Project_Decomposition/conversions.py)
