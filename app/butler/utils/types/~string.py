
def startswith(item, sub, beg = 0, end = None, **kwargs):
	end = end if end else len(item)
	return item.startswith(sub, beg, end)

def contains(item, sub, beg = 0, end = None, **kwargs):
	end = end if end else len(item)
	return sub in item[beg:end]

def endswith(item, sub, beg = 0, end = None, **kwargs):
	end = end if end else len(item)
	return item.endswith(sub, beg, end)

def notstartswith(item, sub, beg = 0, end = None, **kwargs):
	end = end if end else len(item)
	return False if item.startswith(sub, beg, end) else True


def notcontains(item, sub, beg = 0, end = None, **kwargs):
	end = end if end else len(item)
	return False if sub in item[beg:end] else True

def notendswith(item, sub, beg = 0, end = None, **kwargs):
	end = end if end else len(item)
	return False if item.endswith(sub, beg, end) else True