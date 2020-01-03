import datetime
import subprocess
import random
import os
import sys


def main():
    # path to file
    file_path = os.path.realpath("text.txt");

    # Set max to one for a single commit on each run or 
    # randomly generate a max number of commits each run
    num_args = len(sys.argv)
    base = int(10 if num_args <= 2 else int(sys.argv[2]))
    try:
        count = random.randint(1, 5) if num_args <= 1 else int(sys.argv[1], base)
    except ValueError as error:
        print(error)

    while count > 0:

        # gets current time and date at execution time
        content = str(datetime.datetime.now())

        # Discard changes and pull from master
        subprocess.run(["git", "reset", "--hard", "origin/master"])
        subprocess.run(["git", "pull", "origin", "master"])

        # Edit text file
        with open(file_path, "w") as file:
            file.write(content)

        # Git Add
        subprocess.run(["git", "add", "."])

        # Git Commit
        subprocess.run(["git", "commit", "-m", "Updated text.txt"])

        # Git Push
        subprocess.run(["git", "push"])

        count -= 1

if __name__ == "__main__":
    main()
