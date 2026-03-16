import os
import shutil
os.makedirs("first/second/third", exist_ok=True)

path = "."
for item in os.listdir(path):
    fullpath = os.path.join(path, item)

    if os.path.isdir(fullpath):
        print("D:", item)
    else:
        print("F:", item)

folder = "first/second"
for file in os.listdir(folder):
    if file.endswith(".txt"):
        print(file)

old = "first/second/third/text.txt"
new = "first/second/text.txt"
os.rename(old, new)
print("File moved successfully")

import shutil

old = "first/test.txt"
new = "first/second/third/text.txt"
shutil.copy(old, new)
print("File copied successfully")