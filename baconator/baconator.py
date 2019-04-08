import random

from baconator.names import FIRST_NAMES, LAST_NAMES


def generate(delimiter: str = '-', token_len: int = 4):
    items = [random.choice(FIRST_NAMES).replace('_', delimiter),
             random.choice(LAST_NAMES).replace('_', delimiter)]
    if token_len > 0:
        token = random.randrange(10 ** token_len)
        items.append('{:0>{w}}'.format(token, w=token_len))
    return delimiter.join(items)
