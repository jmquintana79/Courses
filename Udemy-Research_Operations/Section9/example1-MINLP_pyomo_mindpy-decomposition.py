import pyomo.environ as pyo
from pyomo.environ import *
from pyomo.opt import SolverFactory

# create model
model = pyo.ConcreteModel()

# define variables
model.x = pyo.Var(within=Integers, bounds=(0,10))
model.y = pyo.Var(bounds=(0,10))
x = model.x
y = model.y

# define constraints
model.C1 = pyo.Constraint(expr= -x+2*y*x<=8)
model.C2 = pyo.Constraint(expr= 2*x+y<=14)
model.C3 = pyo.Constraint(expr= 2*x-y<=10)

# define objective function
model.obj = pyo.Objective(expr= x+y*x, sense=maximize)

# solver election = DECOMPOSITION
opt = SolverFactory('mindtpy')
# linear and non-linear solvers selection and urn
opt.solve(model, mip_solver='cbc', nlp_solver='ipopt')

# print model
model.pprint()

# collect results
x_value = pyo.value(x)
y_value = pyo.value(y)

# display results
print('\n---------------------------------------------------------------------')
print('x=',x_value)
print('y=',y_value)