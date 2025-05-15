# The main idea is to count all the occurring characters in a string. If you have
# a string like aba, then the result should be {'a': 2, 'b': 1}.

# What if the string is empty? Then the result should be empty object literal, {}.

import numpy as np


def count(s):
    chars, counts = np.unique(list(s), return_counts=True)
    return {c: cnt for c, cnt in zip(chars, counts)}
