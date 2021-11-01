import pyomo.environ as pyo
from pyomo.environ import *
from pyomo.opt import SolverFactory

# create model object
model = pyo.ConcreteModel()

# create variables
model.x = pyo.Var(bounds=(0,10))
model.y = pyo.Var(bounds=(0,10))
x = model.x
y = model.y

# create constrains
model.C1 = pyo.Constraint(expr= -x+2*y<=8)
model.C2 = pyo.Constraint(expr= 2*x+y<=14)
model.C3 = pyo.Constraint(expr= 2*x-y<=10)

# objective function (maximization)
model.obj = pyo.Objective(expr= x+y, sense=maximize)

# solver selection
opt = SolverFactory('glpk')

# launch optimization
opt.solve(model)

# print model information
model.pprint()

# get best solution
x_value = pyo.value(x)
y_value = pyo.value(y)

# display
print('\n-------------------------------------------------------------------')
print('Best solution:')
print('x=',x_value)
print('y=',y_value)