# Training C - Git & GitHub

## Background

* Git is a version control tool that is used for configuration management of software files.
  * The collection of files is called a repository.
  * A new or changed file is not added to the repository until the developer commit's it.
  * The repository maintains the history of all commits added to the repository.
  
* GitHub is a place to share Git repositories in the cloud.
  * You can share commits from your computer into the cloud by pushing.
  * You can merge commits from the cloud into your computer by pulling.
  * Useful for team projects or using multiple computers for development.
  * It's usually best to use the IDE to publish to GitHub.  This will automatically create the repository, commit the files, and publish to GitHub.  Make sure your `.gitignore` is setup properly first.

![workflow](workflow.drawio.png)

* Working on Teams
  * To avoid putting broken or unfinished code into the repository, consider using a branch.
  * You will commit, pull, and push with your branch until it works.  When finished, you will merge your branch for the whole team to use.

![workflow](workflow_team.drawio.png)

* Common Git Commands:

| Command                                      | Description                                                                   |
|----------------------------------------------|-------------------------------------------------------------------------------|
| `git clone <url>`                            | Copy a shared repository from GitHub to your computer.                        |
| `git init`                                   | Create a new repository on your computer.                                     |
| `git add <file>`                             | Stage new or modified file in preparation to commit to your repository.       |
| `git add .`                                  | Stage all new and modified files in preparation to commit to your repository. |
| `git commit -m <message>`                    | Commit all staged files to the repository.                                    |
| `git pull`                                   | Merge all changes from GitHub into the repository on your computer.           |
| `git push`                                   | Publish all changes from the repository on your computer to GitHub.           |
| `git push -u origin main`                    | Used to push the very first time to GitHub.                                   |
| `git remote add origin <url>`                | Specify the GitHub url associated with the repository on your computer.       |
| `git status`                                 | Report showing which files need to be committed.                              |
| `git log --oneline`                          | Report showing all commits made to the repository.                            |
| `git revert <commit>`                        | To undo a commit of a specific commit.                                        |
| `git rm --cached <file>`                     | Remove a file from the repository but keep a copy in your folder.             |
| `git checkout -b <name>`                     | Create a new branch in the repository on your computer and open it.           |
| `git checkout <name>`                        | Open a branch you already created in the repository on your computer.         |
| `git checkout main`                          | Open the main branch in the respository on your computer.                     |
| `git push -u origin <name>`                  | Used to push a branch for the first time to GitHub.                           |
| `git rebase main`                            | Used to merge changes from the main branch into your branch.                  |
| `git merge <name>`                           | Used to merge changes from your branch into the main branch.                  |
| `git branch -d <name>`                       | Used to delete a branch after it has been merged.                             |
| `git config --global user.name <your name>`  | Set your name in the configuration on your computer.                          |
| `git config --global user.email <your email>`| Set your email in the configuration on your computer.                         |

## Example

1. Install Git on your computer: [https://git-scm.com/](https://git-scm.com/)

1. Set your name and email into the Git configuration.

1. Create a GitHub account: [https://github.com/](https://github.com/)

1. Make sure you have a `README.md` and a `.gitignore` file in the top folder of your project.

1. Open your project in Visual Studio Code and publish your project as a public repository in GitHub.

1. Make a change to your project and from the terminal:

    * View the status of changes
    * Stage your change
    * View the status of changes
    * Commit your change
    * View the log to see your commit
    * Push your change
    * Verify the change in GitHub

1. Repeat the previous step but use the built-in tools in Visual Studio Code.

## Discussion

What will the benefits be of dilligently using Git and GitHub with your personal project.
