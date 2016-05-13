from os.path import expanduser

$home = 2000

config_path = expanduser("~/.butler/config.json")
with open(config_path, 'r') as f:
	print(f.read())