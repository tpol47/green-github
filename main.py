import datetime
import subprocess

# path to directory
path = "C:\\Users\\Nick\\Documents\\VS Code\\GreenGitHub\\text.txt"

# gets current time and date at execution time
content = str(datetime.datetime.now())

print("---- Git Status ----")
subprocess.run(["git", "status"])

print("---- Git Pull ----")
subprocess.run(["git", "pull"])

print("---- Editing File ----")
f=open(path, "w")
f.write(content)
f.close()

print("---- Git Add ----")
subprocess.run(["git", "add", "."])

print("---- Git Commit ----")
subprocess.run(["git", "commit", "-m", "\"Updated text.txt\""])