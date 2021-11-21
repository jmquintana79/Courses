import numpy as np
from pymoo.core.problem import ElementwiseProblem
from pymoo.factory import get_termination
from pymoo.algorithms.moo.nsga2 import NSGA2
from pymoo.factory import get_sampling, get_crossover, get_mutation
from pymoo.optimize import minimize
 

#%% PROBLEMA DEFINITION

class MyProblem(ElementwiseProblem):
     
    def __init__(self):
        super().__init__(n_var=2,              # number of variables
                         n_obj=2,              # number of objective functions
                         n_constr=2,           # number of constraings
                         xl=np.array([-2,-2]), # lower bound
                         xu=np.array([2,2]))   # upper bound
 
    def _evaluate(self, x, out, *args, **kwargs):
        ## objective functions
        #   in this case is minimization --> to maximize, just multiply by -1 the equation
        f1 = 100 * (x[0]**2 + x[1]**2)
        f2 = (x[0]-1)**2 + x[1]**2
 
        ## constrains functions
        #   in this case is <= 0 --> you can convert a >= constraint to <= multiplying it by -1
        g1 = 2*(x[0]-0.1) * (x[0]-0.9) / 0.18
        g2 = - 20*(x[0]-0.4) * (x[0]-0.6) / 4.8
 
        # store functions
        out["F"] = [f1, f2]
        out["G"] = [g1, g2]
 
problem = MyProblem()
 

#%% MODEL DEFINITION AND LAUNCH

# parameters
algorithm = NSGA2(
    pop_size=40,
    n_offsprings=10,
    sampling=get_sampling("real_random"),
    crossover=get_crossover("real_sbx", prob=0.9, eta=15),
    mutation=get_mutation("real_pm", eta=20),
    eliminate_duplicates=True
)
 
# termination criteria (stop criterium)
termination = get_termination("n_gen", 40)
 
#solve problem
res = minimize(problem,
               algorithm,
               termination,
               seed=1,
               save_history=True,
               verbose=True)
 

#%% GET RESULTS

#get solutions
X = res.X
F = res.F

#%% PLOT PARETO FRONT
# In this case it is possible this plot because there are only 2 objective functions

import matplotlib.pyplot as plt
plt.figure(figsize=(7, 5))
plt.scatter(F[:, 0], F[:, 1], s=30, facecolors='none', edgecolors='blue')
plt.title("Objective Space")
plt.xlabel("f1")
plt.ylabel("f2")
plt.show()

# Now, to define the best solution, you can use the variables X and F to create your own criteria. For example you can find the point (F1,F2) that is closest to the origin point (0,0), or any other criteria.

