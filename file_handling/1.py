import shutil
import os
with open("read.txt", "w") as f:
    f.write("Hello, my name is Beibarys\n")
    f.write("I am studying at KBTU ")

with open("read.txt", "r") as f:
    print(f.read())

with open("read.txt", "a") as f:
    f.write("And my hobby is editing videos\n")

with open("read.txt", "r") as f:
    print(f.read())

shutil.copy("read.txt", "read_copy.txt")

shutil.copy("read.txt", "read_backup.txt")

file = "read_copy.txt"
if os.path.exists(file):
    os.remove(file)