import pandas as pd, numpy as np
from geneticalgorithm import geneticalgorithm as ga

#inputs
nodes = pd.read_excel('route_inputs.xlsx', sheet_name='nodes')
paths = pd.read_excel('route_inputs.xlsx', sheet_name='paths')
nVars = len(paths)

#%% PROBLEM DEFINITION

#fitness function
def f(x):
    # initialize penalization
    pen = 0
    
    ## constraint sum(x) == 1 (origin)
    
    # node origin (=1)
    node_origin = int(nodes.node[nodes.description=='origin'])
    # paths indexes from origin
    i_paths_from_origin = paths.index[paths.node_from==node_origin]
    # constraint
    if sum([x[p] for p in i_paths_from_origin]) != 1:
        # set penalization 
        pen += 1000000 * np.abs(sum([x[p] for p in i_paths_from_origin]) - 1)
    
    
    ## constraint sum(x) == 1 (destination)
    
    # node final destination (=7)
    node_destination = int(nodes.node[nodes.description=='destination'])
    # paths indexes to destination
    i_paths_to_destination = paths.index[paths.node_to==node_destination]
    # constraing
    if sum([x[p] for p in i_paths_to_destination]) != 1:
        # set penalization
        pen += 1000000 * np.abs(sum([x[p] for p in i_paths_to_destination]) - 1)
    
    
    ## constraint sum(x, in) == sum(x, out)
    
    # nodes between origin and destination
    nodes_between_origin_destination = nodes.node[nodes.description=='middle point']
    for node in nodes_between_origin_destination:
        # in summation
        sum_in = sum([x[p] for p in paths.index[paths.node_to==node]])
        # out summatioin
        sum_out = sum([x[p] for p in paths.index[paths.node_from==node]])
        # constraint
        if sum_in != sum_out:
            # set penalization
            pen += 1000000 * np.abs(sum_in - sum_out)

    #objective function and return (minimize)
    objFun = sum([x[p] * paths.distance[p] for p in paths.index])
    return objFun + pen

# variables 1x8 (nVars) bounds definition (yes / no)
varbounds = np.array([[0,1]]*nVars)
# variables types definition
vartype = np.array([['int']]*nVars)

#%% MODEL DEFINITION & LAUNCH

#GA parameters
algorithm_param = {'max_num_iteration': 500,\
                   'population_size':100,\
                   'mutation_probability':0.30,\
                   'elit_ratio': 0.10,\
                   'crossover_probability': 0.50,\
                   'parents_portion': 0.30,\
                   'crossover_type':'uniform',\
                   'max_iteration_without_improv':100}

# solver
model = ga(function=f,
           dimension=nVars,
           variable_type_mixed=vartype,
           variable_boundaries=varbounds,
           algorithm_parameters=algorithm_param)
## launch solver
model.run()


#%% GET RESULTS

# display results
x = model.best_variable
objFun = model.best_function
paths['activated'] = 0
for p in paths.index:
    paths.activated[p] = x[p]

print('\n\nAll Paths:')
print(paths)

print('\nSelected Paths:')
print(paths[paths.activated==1])

print('\nTotal path (total distance of the most optimal path):', objFun)