import pyomo.environ as pyo
from pyomo.environ import *
from pyomo.opt import SolverFactory
import pandas as pd

# inputs
dataGen = pd.read_excel('inputs.xlsx', sheet_name='gen')
dataLoad = pd.read_excel('inputs.xlsx', sheet_name='load')
Ng = len(dataGen)

# model
model = pyo.ConcreteModel()

# define variable with Ng dimessions
model.Pg = pyo.Var(range(Ng), bounds=(0,None))
# this is to do easier to build equations later
Pg = model.Pg
# display variable
print(f'variable (num dim = {len(model.Pg)}):') # model.Pg is a array
model.Pg.pprint()

# constraints: balance
pg_sum = sum([Pg[g] for g in dataGen.id])
print(f'sumatorio de la variable: "{pg_sum}"')
model.balance = pyo.Constraint(expr = pg_sum == sum(dataLoad.value))
# display balance
print('constrain (balance):') 
model.balance.pprint()

# constraints: condition
model.cond = pyo.Constraint(expr = Pg[0]+Pg[3] >= dataLoad.value[0])
# display constrain
print('constrain (condition):') 
model.cond.pprint()

# constraints: limits
model.limits = pyo.ConstraintList()
for g in dataGen.id:
    model.limits.add(expr = Pg[g] <= dataGen.limit[g])
# display constrain
print('constrain (limits):') 
model.limits.pprint()

# objective function
cost_sum = sum([Pg[g]*dataGen.cost[g] for g in dataGen.id])
model.obj = pyo.Objective(expr = cost_sum)

# select solver
opt = SolverFactory('cbc')
# launch solver
results = opt.solve(model)

# store results
dataGen['Pg'] = [pyo.value(Pg[g]) for g in dataGen.id]
# display
print('results:')
print(dataGen)

# display summary
print(results)



