import pyomo.environ as pyo
import numpy as np
import time
from pyomo.environ import *
from pyomo.opt import SolverFactory

# create model
model = pyo.ConcreteModel()

# create variables
model.x = pyo.Var(bounds=(-np.inf,3))
model.y = pyo.Var(bounds=(0,np.inf))
x = model.x
y = model.y

# create constrains
model.C1 = pyo.Constraint(expr= x+y<=8)
model.C2 = pyo.Constraint(expr= 8*x+3*y>=-24)
model.C3 = pyo.Constraint(expr= -6*x+8*y<=48)
model.C4 = pyo.Constraint(expr= 3*x+5*y<=15)

# objective function definition
model.obj = pyo.Objective(expr= -4*x-2*y, sense=minimize)

# initial time counting
tic = time.time()
opt = SolverFactory('cbc')
opt.solve(model)
# final time counting
toc = time.time()
# spent time
tictoc = toc-tic

# get results
x_value = pyo.value(x)
y_value = pyo.value(y)

# display
print('time spent:',tictoc)
print('x:',x_value)
print('y:',y_value)