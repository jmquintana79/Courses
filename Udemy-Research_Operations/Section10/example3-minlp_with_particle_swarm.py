import numpy as np
from pyswarm import pso

"""
Mixed-Integer Non-Linear Problem solved with Particle Swarm.
    variable - 1x2
"""


#%% PROBLEM DEFINITION

# fitness function
def model_obj(x):
    # initialize penalization
    pen = 0
    # define x[0] as an integer
    x[0] = np.round(x[0],0)
    # constraints
    if not -x[0]+2*x[1]*x[0]<=8: pen = np.inf
    if not 2*x[0]+x[1]<=14: pen = np.inf
    if not 2*x[0]-x[1]<=10: pen = np.inf
    # objective function (maximization) + penalization
    return -(x[0]+x[1]*x[0]) + pen

# constrains function (in this case is empty becase they were alreday defined in the fitness function)
def cons(x):
    return []

# bounds definition (lower and upper bounds)
lb = [0,0]
ub = [10,10]
# initial point
x0 = [0,0]

#%% MODEL DEFINITION AND LAUNCH

xopt, fopt = pso(model_obj,lb,ub,x0,cons)


#%% GET RESULTS

print('x =', xopt[0])
print('y =', xopt[1])
# [out]: x = 5.0
# [out]: y = 1.2999999992167612