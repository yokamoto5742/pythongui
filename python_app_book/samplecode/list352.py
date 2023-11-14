import os

if os.path.exists("python_gui_secondstep"):
    print("That location exists!")
else:
    os.mkdir("python_gui_secondstep")
    print("Location created!")
