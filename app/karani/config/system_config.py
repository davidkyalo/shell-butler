from karani import utils
from . import base, const


class System(base.Configuration):

	"""docstring for System"""

	def __getattr__(self, key):
		uckey = key.upper()
		if hasattr(const, uckey):
			return getattr(const, uckey, None)
		else:
			return super(System, self).__getattr__(key)
