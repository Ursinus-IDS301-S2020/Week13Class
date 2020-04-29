#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
An example of a Markov model that uses
a dictionary instead of a matrix, which
makes it more readable and easier to specify
"""

import numpy as np

def pick_random_element(prob):
    """
    Parameters
    ----------
    prob: {string: double}
        A dictionary of all transition
        probabilities from some state
        we're in to all other states
    Returns
    -------
    The next character, sampled according
    to the probabilities
    """
    keys = list(prob.keys())
    probs = np.array(list(prob.values()))
    probs = np.cumsum(probs)
    r = np.random.rand()
    idx = np.searchsorted(probs, r)
    return keys[idx]

probs = {
        'a':{'a':0.3,
             'b':0.5,
             'c':0.2
             },
         'b':{'b':0.9,
              'c':0.1},
          'c':{'a':0.5,
               'd':0.5
              },
          'd':{'d':1}
        }
  
state = 'a'
num_samples = 100
for i in range(num_samples):
    print(state, end='')
    state = pick_random_element(probs[state])
