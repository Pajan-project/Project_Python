import random
import string

def pk(panjang:int):
    Index = "".join(random.choice(string.ascii_letters) for i in range(panjang))
    return Index