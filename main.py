import datetime
import subprocess
import os

# path to directory
path = "C:\\Users\\Nick\\Documents\\VS Code\\GreenGitHub

# path to file
file_path = "C:\\Users\\Nick\\Documents\\VS Code\\GreenGitHub\\text.txt"

# gets current time and date at execution time
content = str(datetime.datetime.now())

# Discard changes and pull from master
subprocess.run(["git", "reset", "--hard", "origin/master"])
subprocess.run(["git", "pull", "origin", "master"])

# Edit text file
f=open(file_path, "w")
f.write(content)
f.close()

# Git Add
subprocess.run(["git", "add", "."])

# Git Commit
subprocess.run(["git", "commit", "-m", "Updated text.txt"])

# Git Push
subprocess.run(["git", "push"])