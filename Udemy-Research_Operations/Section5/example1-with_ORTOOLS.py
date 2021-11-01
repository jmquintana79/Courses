#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 10 16:42:52 2021

@author: juan

ORTOOLS:
Very simple framework but only for Linear problems.

SOLVER OPTIONS FOR THIS LINEAR PROBLEM:
- GLOP: Linear solver from Google.
- Gurobi: Another linear solver very fast (now it is not isntalled).

"""

from ortools.linear_solver import pywraplp

# create solver
solver = pywraplp.Solver.CreateSolver('GLOP')

# create variables
x = solver.NumVar(0, 10, 'x')
y = solver.NumVar(0, 10, 'y')
 
# create constrains
solver.Add(-x+2*y<=8)
solver.Add(2*x+y<=14)
solver.Add(2*x-y<=10)

# objective function definition
solver.Maximize(x+y) 
# in case of wanting to minimiza, just replace with Minimize

# get results
results = solver.Solve()

# check if the result is the optimal
if results == pywraplp.Solver.OPTIMAL:
    print('Optimal found.')

# display results
print(f'x = {x.solution_value()}')
print(f'y = {y.solution_value()}')
