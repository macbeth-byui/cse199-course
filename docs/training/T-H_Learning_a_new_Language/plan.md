# Training H - Learning a New Language

## Background

* One benefit of learning to code is that it enables you to quickly learn new languages.

* Most all languages have the same types of tools:
  * Loops
  * Variables
  * Functions
  * Input/Output
  * Data Structures (e.g. Lists)

* To learn a new language:
  1. Setup your environment
  2. Write the `Hello World` program
  3. Take a simple program in the language you know and then rewrite it in the language you want to learn.

## Example

1. Goto GitHub and create a new private repository called `Learning`.

1. After the repository is created, click on `Create a codespace`.  This will start a virtual environment online using Visual Studio Code.

1. Implement `Hello World` in Python, C#, and C++.  Make sure you install the Visual Studio Code extensions when prompted.  Notice how each language uses a different syntax but has the same base components.

1. Copy the following code into a file called `stats.py`:

    ```python
    def average(numbers):
    total = 0
    for number in numbers:
        total += number
    avg = total / len(numbers)
    return avg

    def main():
        my_numbers = [3,1,6,3,5,4,6,2]
        my_avg = average(my_numbers)
        print(f"Average = {my_avg}")

    if __name__ == "__main__":
        main()
    ```

1. Rewrite the code using C# and then rewrite it using C++.

## Solution

* [hello.py](hello.py)
* [hello.cs](hello.cs)
* [hello.cpp](hello.cpp)
* [stats.py](stats.py)
* [stats.cs](stats.cs)
* [stats.cpp](stats.cpp)
