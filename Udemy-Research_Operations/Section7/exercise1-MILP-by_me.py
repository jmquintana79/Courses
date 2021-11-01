import pyomo.environ as pyo
from pyomo.environ import *
from pyomo.opt import SolverFactory


# model
model = pyo.ConcreteModel()

# define variables
model.x = pyo.Var(range(1,6,1), within=Integers, bounds=(0,None))
model.y = pyo.Var(bounds = (0, None))
x = model.x
y = model.y
print('\nvariables:')
model.x.pprint()
model.y.pprint() 

# constraint 1
x_sum = sum([x[i] for i in range(1,6,1)])
model.c1 = pyo.Constraint(expr = x_sum + y <= 20)
# display balance
print('\nconstrain 1:') 
model.c1.pprint()

# constraints 2
model.c2 = pyo.ConstraintList()
for i in range(1,6,1):
    model.c2.add(expr = x[i] + y >= 15)
# display constrain
print('\nconstrain 2 (list):') 
model.c2.pprint()

# constraint 3
ix_sum = sum([i*x[i] for i in range(1,6,1)])
model.c3 = pyo.Constraint(expr = ix_sum >= 10)
# display balance
print('\nconstrain 3:') 
model.c3.pprint()

# constraint 4
model.c4 = pyo.Constraint(expr = x[5] + 2*y >= 30)
# display balance
print('\nconstrain 4:') 
model.c4.pprint()


# objective function
model.obj = pyo.Objective(expr = sum([x[i] for i in range(1,6,1)])+y, sense=minimize)

# select solver
opt = SolverFactory('cbc')
# launch solver
opt.solve(model)

# display
print('\nmodel:') 
model.pprint()

# get optimal results and display
print(f'\n{"-"*50}')
for i in range(1,6):
    print('x[%i] = %i' % (i, pyo.value(x[i])))
print('y = %.2f' % pyo.value(y))
print('Obj = ', pyo.value(model.obj))



