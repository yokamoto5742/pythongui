import os
import shutil

folder_name = "mvFolder"

if not os.path.exists(folder_name):
    os.mkdir(folder_name)
else:
    for file in os.listdir("testFolder"):
        if file.endswith(".txt"):
            path = os.path.join("testFolder", file)
            shutil.move(path, "mvFolder")
