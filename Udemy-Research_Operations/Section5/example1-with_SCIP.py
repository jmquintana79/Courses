#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 10 16:42:52 2021

@author: juan

SCIP:
- It is not possible choose the solver.
- Linear and Non-Linear problems are possible.
- In consecuences, it is not necessary set up nothing, the framework will do 
it automatically.

"""

from pyscipopt import Model

# create model object
model = Model('exemplo')

# create variables
x = model.addVar('x',lb=0,ub=10)
y = model.addVar('y',lb=0,ub=10)

# objective function definition
model.setObjective(x+y, sense='maximize')

# create constrains
model.addCons(-x+2*y<=8)
model.addCons(2*x+y<=14)
model.addCons(2*x-y<=10)

# launch optimization
model.optimize()

# get results
sol = model.getBestSol()

# display results
print('\nBest solution:')
print('x=',sol[x])
print('y=',sol[y])