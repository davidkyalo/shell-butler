from karani.utils.types import stack, SingleTone, File
from karani import utils

from .const import *

import json

class ReadOnlyOption(Exception):
	def __init__(self, obj, option):
		cls = obj.__class__.__name__
		msg = "Configuration Error [{0}]: Can't set protected option '{1}'".format(cls, option)
		super(ReadOnlyOption, self).__init__(msg)



class Configuration(SingleTone):
	"""docstring for Configuration"""
	__guarded__ = None
	# __dynamic__ = False
	__strict__ = True

	def __init__(self):
		self.initialize()
		self._has_initialized = True
		self._set_option_overrides()
		self.loaded()

	def initialize(self):
		pass

	def loaded(self):
		pass

	@property
	def homedir(self):
	    return utils.userpath(self._user_home_dir)

	def homepath(self, *paths):
		return utils.joinpaths( self.homedir, *paths)


	def _set_user_options(self):
		file = self._get_user_options_file()
		options = self._load_user_options( file.content if file.exists else None )
		if options:
			self._setopts(**options)

	def _get_user_options_file(self):
		filename = utils.snake_case(self.__class__.__name__) + '.conf'
		return File(location = USER_PREFERENCES_HOME, name = filename)


	def _load_user_options(self, content = None):
		if not content:
			return None
		return json.loads(content)


	def get(self, option, default = None):
		return getattr(self, option, default)

	def set(self, _key_ = None, _value_ = None, **options):
		if not _key_:
			self._setopts(**options)
		else:
			self._setopt( _key_, _value_ )

	@classmethod
	def _get_guarded_options(cls):
		return cls.__guarded__ if cls.__guarded__ else []

	def _is_guarded(self, key):
		return (key in self._get_guarded_options())

	def _is_protected(self, key):
		return ( key.startswith('_') or self._is_guarded(key) )

	def _setopt(self, key, value, unguard = False):
		if unguard or not self._is_protected(key):
			setattr(self, key, value)
		elif self.__strict__:
			raise ReadOnlyOption(self, key)


	def _setopts(self, _unguard_ = False, **options):
		for key, value in options.items():
			self._setopt(key, value, _unguard_)


	def __getitem__(self, key):
		return getattr(self, option)

	def __getattr__(self, key):
		if key.startswith('_'):
			if key in self.__dict__:
				return self.__dict__[key]
			elif self.__strict__:
				raise AttributeError('[{0}] Configuration key "{1}" does not exist')
			else:
				return None
		else:
			return getattr(self, '_' + key)