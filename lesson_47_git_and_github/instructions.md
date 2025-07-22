# Lesson 47: Version Control with Git & GitHub

Version Control Systems (VCS) are essential tools for software development, allowing teams to track changes, collaborate efficiently, and manage different versions of their codebase. **Git** is the most widely used distributed version control system, and **GitHub** is the most popular web-based platform for hosting and collaborating on Git repositories.

---

### Why Version Control?

*   **Tracking Changes**: Keep a history of every modification made to your code.
*   **Collaboration**: Multiple developers can work on the same project simultaneously without overwriting each other's work.
*   **Branching and Merging**: Create separate lines of development (branches) for new features or bug fixes, and then integrate them back into the main codebase.
*   **Rollbacks**: Easily revert to previous versions of your code if something goes wrong.
*   **Backup**: Your code is stored remotely, providing a backup.

### Key Git Concepts

*   **Repository (Repo)**: A project folder that Git tracks. It contains all the project files and the entire history of changes.
*   **Commit**: A snapshot of your repository at a specific point in time. Each commit has a unique ID, a message, and points to its parent commit(s).
*   **Branch**: A lightweight movable pointer to a commit. It represents an independent line of development.
*   **Master/Main**: The default development branch in a Git repository.
*   **Head**: A pointer to the latest commit in the current branch.
*   **Working Directory**: The files you see and edit on your local machine.
*   **Staging Area (Index)**: An area where you prepare changes before committing them. You add files to the staging area using `git add`.
*   **Remote Repository**: A version of your repository hosted on a server (e.g., GitHub), allowing for collaboration and backup.

### Basic Git Commands

Before you start, ensure Git is installed on your system. You can download it from [git-scm.com](https://git-scm.com/).

#### 1. `git init` - Initialize a new Git repository

This command creates a new, empty Git repository in the current directory.

```bash
mkdir my_project
cd my_project
git init
# Output: Initialized empty Git repository in /path/to/my_project/.git/
```

#### 2. `git clone <repository_url>` - Clone an existing repository

Downloads an existing Git repository from a remote server to your local machine.

```bash
git clone https://github.com/octocat/Spoon-Knife.git
# This will create a new directory named Spoon-Knife with the repository content.
```

#### 3. `git add <file(s)>` - Stage changes

Adds changes from your working directory to the staging area, preparing them for the next commit.

```bash
echo "Hello, Git!" > hello.txt
git add hello.txt
# Or to add all changes in the current directory:
# git add .
```

#### 4. `git commit -m "<message>"` - Record changes

Saves the staged changes to the repository with a descriptive message.

```bash
git commit -m "Initial commit: Add hello.txt"
# Output: [master (root-commit) ...] 1 file changed, 1 insertion(+)
```

#### 5. `git status` - Check the status

Shows the status of your working directory and staging area. It tells you which changes are staged, unstaged, or untracked.

```bash
git status
# Output: On branch master
# No commits yet
# Changes to be committed:
#   (use "git rm --cached <file>..." to unstage)
#       new file:   hello.txt
```

#### 6. `git diff` - Show changes

Shows the differences between the working directory and the staging area, or between commits.

```bash
echo "New line." >> hello.txt
git diff
# Output will show the added line in red/green.
```

#### 7. `git log` - Show commit history

Displays a list of past commits, including their IDs, authors, dates, and messages.

```bash
git log
# Output: commit <commit_id>
# Author: Your Name <your_email@example.com>
# Date:   Mon Jul 22 10:00:00 2024 +0000
#
#    Initial commit: Add hello.txt
```

#### 8. `git branch` - List, create, or delete branches

```bash
git branch # List all branches
# Output: * master

git branch new-feature # Create a new branch

git branch -d old-branch # Delete a branch
```

#### 9. `git checkout <branch_name>` / `git switch <branch_name>` - Switch branches

Switches your working directory to a different branch. `git switch` is a newer, safer alternative to `git checkout` for switching branches.

```bash
git switch new-feature # Switch to new-feature branch
# Output: Switched to branch 'new-feature'
```

#### 10. `git merge <branch_name>` - Join branches

Integrates changes from one branch into the current branch.

```bash
git switch master
git merge new-feature
# Output: Updating ...
# Fast-forward
# ...
```

### Working with Remote Repositories (GitHub)

#### 1. Creating a Repository on GitHub

*   Go to [github.com](https://github.com/) and log in.
*   Click the `+` sign in the top right corner and select `New repository`.
*   Give it a name, an optional description, and choose public/private.
*   **Do NOT initialize with a README, .gitignore, or license if you are linking an existing local repo.**
*   Click `Create repository`.

#### 2. `git remote add origin <repository_url>` - Link local to remote

Connects your local repository to the remote repository on GitHub. `origin` is the conventional name for the primary remote.

```bash
git remote add origin https://github.com/your_username/your_repo_name.git
```

#### 3. `git push -u origin <branch_name>` - Upload local commits

Uploads your local commits to the remote repository. The `-u` flag sets the upstream branch, so future `git push` commands don't need `origin <branch_name>`.

```bash
git push -u origin master # Or main, depending on your default branch name
```

#### 4. `git pull origin <branch_name>` - Download remote changes

Fetches changes from the remote repository and merges them into your current local branch.

```bash
git pull origin master
```

### Git Workflow Best Practices

*   **Commit Early, Commit Often**: Make small, atomic commits with clear messages.
*   **Descriptive Commit Messages**: Explain *why* you made the change, not just *what* you changed.
*   **Branch for Features/Bugs**: Always work on a separate branch for new features or bug fixes.
*   **Pull Before Pushing**: Always `git pull` before you `git push` to avoid merge conflicts.
*   **Review Changes**: Use `git status` and `git diff` frequently.

---

### Quiz

1.  **What is the command to save a snapshot of your staged changes to the repository?**
    a) `git add`
    b) `git commit`
    c) `git push`

2.  **What is the purpose of `git push`?**
    a) To download changes from the remote repository.
    b) To upload your local commits to the remote repository.
    c) To create a new repository.

3.  **Which Git command is used to create a new, empty Git repository in the current directory?**
    a) `git clone`
    b) `git init`
    c) `git new`

4.  **If you want to get the latest changes from a remote repository and merge them into your current local branch, which command would you use?**
    a) `git fetch`
    b) `git pull`
    c) `git merge`

<details>
  <summary><b>Answer Key</b></summary>
  1. b
  2. b
  3. b
  4. b
</details>