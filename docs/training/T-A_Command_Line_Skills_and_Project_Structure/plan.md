# Training A - Command Line Skills and Project Structure

## Background

* It is important to know where your files are on your computer:
  * Documents organized by class and/or project - Synched Cloud Storage (e.g. OneDrive) is encouraged
  * Code organized by class and/or project - Recommend that you do not put in Synched Cloud Storage.  Use GitHub instead.

* Most Integrated Development Environment (IDE) tools have a preferred method of working with code:
  * Visual Studio Code - Open a folder containing a single class or project
  * JetBrains - Open a project file that is self-contained in a single project

* Project structure usually follows a pattern (this will vary based on programming language and/or framework used).  Within your dedicated project folder, you will likely have the following:
  * `README.md` - A markdown file that contains information about your project.
  * `.gitignore` - A text file that contains a list of all files and folders that you don't want included in Git/GitHub.  You will want to put files that contain secret keys and build folders in here.
  * `\src` - Sometimes its useful to organize your code files in this folder.  Often additional sub-folders are needed for larger projects.
  * `\tests` - Sometimes its useful to put tests in a separate folder.  In some languages, its easier to add tests directly to your existing code files.
  * `\assets` - Data files (including database files), pictures, music, and other files used by your software.

* The `PLAY` button in an IDE is convienant, but it is good to know what is happening behind the scenes.  Learn how to use the terminal.

|Description                                              | Terminal Command                    |
|---------------------------------------------------------|-------------------------------------|
|What directory am I in?                                  | `pwd`                               |
|What is in my directory?                                 | `ls`                                |
|How do I change directories?                             | `cd <folder>`                       |
|How do I move back a directory?                          | `cd ..`                             |
|How do I create a new directory?                         | `mkdir <folder>`                    |
|How do I delete a file?                                  | `rm <file>`                         |
|How do I remove an empty directory?                      | `rmdir <folder>`                    |
|How do I rename a file?                                  | `mv <oldfile> <newfile>`            |
|How do I quickly display a file?                         | `cat <file>`                        |
|How do I open the current folder in Visual Studio Code?  | `code .`                            |
|How do I run a python program?                           |                                     |
|                                                         | Win: `py <file.py>`                 |
|                                                         | Mac\Linux: `python3 <file.py>`      |
|How do I install a python library?                       |                                     |
|                                                         | Win: `py -m pip install <library>`  |
|                                                         | Mac\Linux: `pip3 install <library>` |

## Example

1. Open a terminal and create a folder to store all of your code for classes and/or projects.  Do **not** put this folder in a place that is auto-backed up using a tool like OneDrive.  

1. In the terminal, create a sub-folder for your project in your code folder.  Change directory into that folder after you create it.

1. Start Visual Studio Code in your current project folder.

1. Create a `README.md` and a `.gitignore` file in your project

1. Create a file called `main.py` and write code to display `Hello World`.  Run your program from the command line.

1. From the terminal, display the list of files in your project folder.

1. From the terminal, rename the file `main.py` to `hello.py`.  Re-display the list of files in your project folder and re-run your program from the terminal.

1. Create a file called `secret.txt` and put a secret code inside of it.  Add `secret.txt` to your `.gitignore` file.  

1. From the terminal, delete the `secret.txt` file and remove it from the `.gitignore` file.

## Discussion

Why is organization important for you in this project and your future academic and personal projects?