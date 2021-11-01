#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

EXERCISE 1:
    My solution with SCIP.
    
"""

from pyscipopt import Model
import time
tic = time.time()

# create model object
model = Model('exercise1')

# create variables
x = model.addVar('x',ub=3)
y = model.addVar('y',lb=0)

# objective function definition
model.setObjective(-4*x-2*y, sense='minimize')

# create constrains
model.addCons(x+y<=8)
model.addCons(8*x+3*y>=-24)
model.addCons(-6*x+8*y<=48)
model.addCons(3*x+5*y<=15)

# launch optimization
model.optimize()

# get results
sol = model.getBestSol()

# display results
print('\nBest solution:')
print('x=',sol[x])
print('y=',sol[y])

# time spent
toc = time.time()
print("--- %s seconds ---"%(toc - tic))
