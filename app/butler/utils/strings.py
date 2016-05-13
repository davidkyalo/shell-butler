import re

def minifytext(text, linesep = ' '):
    text = text.replace('\\n', linesep).replace("\n", linesep)
    return striptext(text)

def striptext(text):
    text = re.sub(' +',' ', text)
    return text.strip()


def concatext(iterable, sep = ' ', minify = False):
    text = sep.join(iterable)
    return minifytext(text, sep) if minify else striptext(text)


def slugify(text, delimeter = '_' , num = None):
    text = text.lower()
    text = re.sub('[^0-9a-zA-Z]+', ' ', text)

    if num is not None:
        text += ' ' + str(num)

    text = re.sub(' +',' ', text)
    return text.strip().replace(' ',delimeter)

def snake_case(text):
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', text)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()
