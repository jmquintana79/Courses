import pyomo.environ as pyo
from pyomo.environ import *
from pyomo.opt import SolverFactory

# model
model = pyo.ConcreteModel()

# variables definition
model.x = pyo.Var(within=Integers, bounds=(0,10)) # --> integer variable
model.y = pyo.Var(bounds=(0,10))
x = model.x
y = model.y

# constraints definition
model.C1 = pyo.Constraint(expr= -x+2*y<=7)
model.C2 = pyo.Constraint(expr= 2*x+y<=14)
model.C3 = pyo.Constraint(expr= 2*x-y<=10)

# objective function definition
model.obj = pyo.Objective(expr= x+y, sense=maximize)

# solver definition and launch
opt = SolverFactory('cbc')
opt.solve(model)

# display
model.pprint()

# get optimal results
x_value = pyo.value(x)
y_value = pyo.value(y)

# display results
print('\n---------------------------------------------------------------------')
print('x=',x_value)
print('y=',y_value)