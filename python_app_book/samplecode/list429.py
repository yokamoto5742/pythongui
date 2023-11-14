import subprocess
import configparser

config = configparser.ConfigParser()


def run1_func():
    config.read("config.ini")
    read_base = config["Run1"]
    app1 = read_base.get("app1")
    app2 = read_base.get("app2")

    programs = [app1, app2]
    for program in programs:
        subprocess.Popen(program)


def run2_func():
    config.read("config.ini")
    read_base = config["Run2"]
    app1 = read_base.get("app1")
    app2 = read_base.get("app2")
    app3 = read_base.get("app3")

    programs = [app1, app2, app3]
    for program in programs:
        subprocess.Popen(program)
