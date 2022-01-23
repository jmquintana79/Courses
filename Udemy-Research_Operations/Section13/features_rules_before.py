import pyomo.environ as pyo
from pyomo.opt import SolverFactory

model = pyo.ConcreteModel()

#Parameter and Sets
model.T = pyo.Param(initialize=10)
T = model.T
model.M = pyo.Param(initialize=4)
M = model.M
model.LimProd = pyo.Param(initialize=10)

model.setT = pyo.RangeSet(1,T)
model.setM = pyo.RangeSet(1,M)


#variables
model.x = pyo.Var(model.setM, model.setT, within=pyo.Integers)
x = model.x

#obj function
model.obj = pyo.Objective(expr = pyo.summation(x), sense=pyo.maximize)

#constraints
model.C1 = pyo.ConstraintList()
for t in model.setT:
    model.C1.add(expr = 2*x[2,t] - 8*x[3,t] <= 0)
    
model.C2 = pyo.ConstraintList()
for t in range(3,T+1):
    model.C2.add(expr = x[2,t] - 2*x[3,t-2] + x[4,t] >= 1)
    
model.C3 = pyo.ConstraintList()
for t in model.setT:
    model.C3.add(expr = sum([x[m,t] for m in range(1,M+1)]) <= 50)

model.C4 = pyo.ConstraintList()
for t in range(2,T+1):
    model.C4.add(expr = x[1,t] + x[2,t-1] + x[3,t] + x[4,t] <= model.LimProd)

model.C5 = pyo.ConstraintList()
for m in range(1,M+1):
    for t in model.setT:
        model.C5.add(pyo.inequality(0, x[m,t], model.LimProd))



#solve
opt = SolverFactory('gurobi')
opt.options['MIPgap'] = 0
opt.options['TimeLimit'] = 10
results = opt.solve(model, tee=True)

print(pyo.value(model.obj))