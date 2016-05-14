import argparse
from collections import deque

class Parser(argparse.ArgumentParser):
	pass


class ChainCommands(argparse.Action):
	"""docstring for ChainCommands"""
	def __call__(self, parser, namespace, values, option_string=None):
		chain = deque( values.split(':') )
		setattr(namespace, self.dest, chain)
		
		
