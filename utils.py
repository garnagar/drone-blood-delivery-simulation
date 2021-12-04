import numpy as np


def min_to_str(min):
    h = int(np.floor(min / 60))
    m = int(np.round(min % 60))
    return "{}:{}".format(h, m)
