import pulp as pl

# create model object (for maximization)
model = pl.LpProblem('Ex', pl.LpMaximize)

# create variables
x = pl.LpVariable('x',0,10)
y = pl.LpVariable('y',0,10)

# create constrains
model += -x+2*y<=8
model += 2*x+y<=14
model += 2*x-y<=10

# objective function (maximization)
model += x+y

# launch optimization (by default use the CBC solver )
status = model.solve()

# get best solution
x_value = pl.value(x)
y_value = pl.value(y)

# display
print('\n-------------------------------------------------------------------')
print('Best solution:')
print('x=',x_value)
print('y=',y_value)