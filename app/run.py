from os.path import expanduser
config_path = expanduser("~/.karani/config.json")
with open(config_path, 'r') as f:
	print(f.read())