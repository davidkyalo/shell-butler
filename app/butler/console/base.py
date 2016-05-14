from .args import Parser
from butler.utils.types import ImportLater

class BaseHandler(object):
	"""docstring for Handler"""
	cmd = None

	childof = None #BaseHandler or ImportLater.
	children = None

	_parser = None
	_parent = None

	def __init__(self, parent = None):
		self._parent = parent

	@property
	def parent(self):
	    return self._parent

	@property
	def parser(self):
		if not self._parser:
			self._parser = self.create_the_parser()
	    return self._parser
	
	def create_the_parser(self):
		kwargs = self.get_default_parser_params()
		custom = self.get_parser_params()
		if custom:
			kwargs.update(custom)
		return Parser(**kwargs)

	def get_parent_parser(self):
		return self.parent.parser if self.parent else None

	def get_default_parser_params(self):
		return dict( prog = self.cmd, parents = self.get_parent_parser() )

	def get_parser_params(self):
		pass

	def handle(self):
		
	
	def initialize(self):
		pass	

	def interact(self):
		pass

	def execute(self):
		pass

	def dispatch(self, handler):
		handler