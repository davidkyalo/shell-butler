from butler.utils import stack
from butler.utils.types import ImportLater



chain_of_command = stack()
unresolved = stack()

def create_node(handler):
	node = stack()
	node.cmd = handler.cmd
	node.childof = handler.childof
	node.cls = handler

	node.children = stack()
	return node



def register(handler):
	node = create_node(handler)
	


def is_registered(handler):


def check_if_registered(handler, raise_err = True):
	