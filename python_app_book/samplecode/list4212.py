import subprocess

def set_func():
    notepad = r"C:\Windows\System32\notepad.exe"
    subprocess.run([notepad, "config.ini"])
