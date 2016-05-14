from butler import utils

USER_HOME = utils.userpath('~/')

KARANI_HOME = utils.joinpaths(USER_HOME, '/.butler')

USER_PREFERENCES_HOME = utils.joinpaths(KARANI_HOME, '/preferences')