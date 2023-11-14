import subprocess


def manual_func():
    subprocess.run(["start", "manual.txt"], shell=True)
