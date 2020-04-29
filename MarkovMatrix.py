#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
An example of using a 2x2 Markov 
matrix of transition probabilities
"""

import numpy as np


probs = np.array([[0.99, 0.01], 
                  [0.01, 0.99]])
states = "ab"
n_draws = 400
state = 0
for i in range(n_draws):
    print(states[state], end='')
    randnum = np.random.rand()
    if randnum < probs[state, 0]:
        state = 0
    else:
        state = 1

