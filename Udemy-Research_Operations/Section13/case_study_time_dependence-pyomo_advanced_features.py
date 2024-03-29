import pyomo.environ as pyo
from pyomo.opt import SolverFactory

# model object
model = pyo.ConcreteModel()
# initialize global parameters
T = 10 # hours
M = 4  # machines

#variables
model.x = pyo.Var(range(1,M+1), range(1,T+1), within=pyo.Integers) # integer because is number of computers
x = model.x

#obj function (maximizar el sumatorio de X para toda maquina m y todas las horas t)
model.obj = pyo.Objective(expr = sum([x[m,t] for m in range(1,M+1) for t in range(1,T+1)]), sense=pyo.maximize)

#constraints
model.C1 = pyo.ConstraintList()
for t in range(1,T+1):
    model.C1.add(expr = 2*x[2,t] - 8*x[3,t] <= 0)
    
model.C2 = pyo.ConstraintList()
for t in range(3,T+1): # para t > 2
    model.C2.add(expr = x[2,t] - 2*x[3,t-2] + x[4,t] >= 1)
    
model.C3 = pyo.ConstraintList()
for t in range(1,T+1):
    model.C3.add(expr = sum([x[m,t] for m in range(1,M+1)]) <= 50)

model.C4 = pyo.ConstraintList()
for t in range(2,T+1): # para t > 1
    model.C4.add(expr = x[1,t] + x[2,t-1] + x[3,t] + x[4,t] <= 10)

model.C5 = pyo.ConstraintList()
for m in range(1,M+1):
    for t in range(1,T+1):
        model.C5.add(expr = x[m,t] <= 10)
        model.C5.add(expr = x[m,t] >= 0)

#solve
#opt = SolverFactory('gurobi')
opt = SolverFactory('glpk',executable='/usr/local/bin/glpsol')
results = opt.solve(model)
# print results
model.pprint()