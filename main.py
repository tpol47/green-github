import datetime
import subprocess
import random

# path to directory
path = "C:\\Users\\Nick\\Documents\\VS Code\\GreenGitHub"

# path to file
file_path = "C:\\Users\\Nick\\Documents\\VS Code\\GreenGitHub\\text.txt"

# Set max to one for a single commit on each run or 
# randomly generate a max number of commits each run
max = 1
# max = random.randint(1,5)

i = 0
while i < max:

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

    i += 1