
class AppMeta(type):
	"""docstring for AppMeta"""
	def __init__(self, arg):
		super(AppMeta, self).__init__()
		self.arg = arg


class Application(object):
	"""docstring for Application"""
	def __init__(self, arg):
		super(Application, self).__init__()
		self.arg = arg
		