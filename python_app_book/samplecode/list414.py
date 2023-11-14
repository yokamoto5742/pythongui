import configparser

config = configparser.ConfigParser()

config.read("config.ini")

read_base = config["Run2"]
print(read_base.get("app3"))
