# Lesson 47: Version Control with Git & GitHub

# This exercise is designed to be completed in your terminal.
# Follow the steps below to practice basic Git and GitHub workflows.

# --- Instructions ---

# 1.  **Create a new directory for your project and navigate into it.**
#     ```bash
#     mkdir my_git_project
#     cd my_git_project
#     ```

# 2.  **Initialize a new Git repository in this directory.**
#     ```bash
#     git init
#     ```

# 3.  **Create a simple file, e.g., `README.md`, and add some content to it.**
#     ```bash
#     echo "# My Awesome Project\n\nThis is a project to learn Git and GitHub." > README.md
#     ```

# 4.  **Check the status of your repository.**
#     ```bash
#     git status
#     ```

# 5.  **Stage the `README.md` file.**
#     ```bash
#     git add README.md
#     ```

# 6.  **Check the status again to see the staged file.**
#     ```bash
#     git status
#     ```

# 7.  **Commit the staged changes with a descriptive message.**
#     ```bash
#     git commit -m "Initial commit: Add README.md"
#     ```

# 8.  **Check the commit history.**
#     ```bash
#     git log
#     ```

# 9.  **Create a new repository on GitHub (or your preferred Git hosting service).**
#     *   Go to [github.com](https://github.com/) and log in.
#     *   Click the `+` sign (top right) -> `New repository`.
#     *   Give it a name (e.g., `my-awesome-project`).
#     *   **IMPORTANT**: Do NOT check "Add a README file", "Add .gitignore", or "Choose a license". You already have a local README.
#     *   Click "Create repository".

# 10. **Link your local repository to the remote repository on GitHub.**
#     *   After creating the repository on GitHub, you will see instructions under "...or push an existing repository from the command line".
#     *   Copy and paste the `git remote add origin <URL>` command into your terminal.
#     *   Example: `git remote add origin https://github.com/YOUR_USERNAME/my-awesome-project.git`

# 11. **Push your local commits to the remote repository.**
#     *   Copy and paste the `git branch -M main` (if your default branch is master) and `git push -u origin main` commands.
#     *   Example: `git push -u origin main` (or `master` if that's your branch name)

# 12. **Verify your push.**
#     *   Refresh your GitHub repository page. You should see your `README.md` file.

# 13. **Make another change, commit, and push.**
#     *   Add another line to your `README.md`:
#         ```bash
#         echo "This is a second line of text." >> README.md
#         ```
#     *   Stage the change:
#         ```bash
#         git add README.md
#         ```
#     *   Commit the change:
#         ```bash
#         git commit -m "Add second line to README"
#         ```
#     *   Push the change:
#         ```bash
#         git push
#         ```
#     *   Verify on GitHub again.

# Congratulations! You've completed a basic Git and GitHub workflow.