import pyomo.environ as pyo
from pyomo.environ import *
from pyomo.opt import SolverFactory

# create model
model = pyo.ConcreteModel()

# define variables
#model.x = pyo.Var(initialize = 0, bounds=(-5,5)) # for "main" local solution
#model.y = pyo.Var(initialize = 0, bounds=(-5,5)) # for "main" local solution
#model.x = pyo.Var(initialize = -5, bounds=(-5,5)) # for another local solution
#model.y = pyo.Var(initialize = 5, bounds=(-5,5)) # for anotes local solution
model.x = pyo.Var(bounds=(-5,5)) # for global solution
model.y = pyo.Var(bounds=(-5,5)) # for global solution
x = model.x
y = model.y

# define objective function
model.obj = pyo.Objective(expr= cos(x+1) + cos(x)*cos(y), sense=maximize)

# solver selection
opt = SolverFactory('ipopt')
# define the tolerance of the error
opt.options['tol'] = 1e-6 # maximum error allowed
# error solver
opt.solve(model)

# print model
model.pprint()

# collect results
x_value = pyo.value(x)
y_value = pyo.value(y)

# display results
print('\n---------------------------------------------------------------------')
print('x=',x_value)
print('y=',y_value)