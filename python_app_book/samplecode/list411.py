import configparser

config = configparser.ConfigParser()

config["Run1"] = {
    "app1": r"C:\Windows\System32\notepad.exe",
    "app2": r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
}

config["Run2"] = {
    "app1": r"C:\Windows\System32\notepad.exe",
    "app2": r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    "app3": r"C:\Windows\System32\mspaint.exe",
}
with open("config.ini", "w+") as file:
    config.write(file)
