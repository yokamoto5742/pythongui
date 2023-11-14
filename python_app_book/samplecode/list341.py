import shutil
import os

try:
    with open("test.txt", "r") as f:
        v = f.read()
except FileNotFoundError:
    print("指定したテキストファイルは見つかりませんでした")
    exit()

if len(v) != 0:
    os.mkdir("txtFolders")
    shutil.move("test.txt", "txtFolders")
else:
    os.remove("test.txt")
