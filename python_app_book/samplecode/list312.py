import subprocess

notepad = r"C:\Windows\System32\notepad.exe"

me = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"

file = r"C:\Users\yokam\OneDrive\デスクトップ\ローカルファイル\test.txt"

programs = [notepad, [me, file]]
for v in programs:
    if isinstance(v, list):
        subprocess.Popen(v)
    else:
        subprocess.Popen(v)
