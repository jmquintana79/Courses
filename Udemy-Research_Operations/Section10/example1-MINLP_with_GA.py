import numpy as np
from geneticalgorithm import geneticalgorithm as ga

"""
MINLP problem solved with GA:
    
    - Variable = array 1x2.

"""

# fitness function
def f(x):
    # initialize penalization
    pen = 0
    # constraints
    if not -x[0]+2*x[1]*x[0]<=8: pen = np.inf
    if not 2*x[0]+x[1]<=14: pen = np.inf
    if not 2*x[0]-x[1]<=10: pen = np.inf
    # objective function (maximization) + penalization
    return -(x[0]+x[1]*x[0]) + pen 

# variable (1x2) bounds 
varbounds = np.array([[0,10],[0,10]])
# variable (1x2) types
vartype = np.array([['int'],['real']])

# algorithm parameters
algorithm_param = {'max_num_iteration': 100,\
                   'population_size':100,\
                   'mutation_probability':0.1,\
                   'elit_ratio': 0.01,\
                   'crossover_probability': 0.5,\
                   'parents_portion': 0.3,\
                   'crossover_type':'uniform',\
                   'max_iteration_without_improv':None}

# model definition
#   function: fitness function.
#   dimension: number of variables.
#   variable_type_mixed: variable types definition.
#   variable_boundaries: variable boundaries definition.
#   algorithm_parameters: algorithm internal parameters.
model = ga(function=f,dimension=2,variable_type_mixed=vartype,variable_boundaries=varbounds,algorithm_parameters=algorithm_param)

# model run (launch solver, display plot of iterations and display best solution)
model.run()
# [out]: best solution = [5.         1.29364262]

