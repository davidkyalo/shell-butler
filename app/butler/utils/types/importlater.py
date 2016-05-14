import importlib

class ImportLater(object):
	"""docstring for LazyModule"""
	def __init__(self, path = None, name = None, module = None, package = None):
		self.name = name
		self.module = module
		self.package = package
		if path:
			self.path = path

		

	def get(self):
		module = importlib.import_module(self.module, self.package)
		return getattr(module, self.name)

	@property
    def path(self):
        return self.module + '.' + self.name

    @path.setter
    def path(self, value):
    	parts = path.split('.')
		self.name = parts[-1]
		self.module = '.'.join(parts[:-1])
