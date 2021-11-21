from ortools.sat.python import cp_model

"""
En este script se pueden hacer dos acciones:
    1. Mostrar todas las soluciones posibles sin optimizar de acuerdo a los
    constrains definidos.
    2. Obtener el resultado mas optimo:
            - descomentar la objective function.
            - comentar el printer del final de todas la soluciones.
"""

# variable solution printer
class VarArraySolutionPrinter(cp_model.CpSolverSolutionCallback):
    """Print intermediate solutions."""

    def __init__(self, variables):
        cp_model.CpSolverSolutionCallback.__init__(self)
        self.__variables = variables
        self.__solution_count = 0

    def on_solution_callback(self):
        self.__solution_count += 1
        for v in self.__variables:
            print('%s=%i' % (v, self.Value(v)), end=' ')
        print()

    def solution_count(self):
        return self.__solution_count


#%% PROBLEM DEFINITION

# model definition
model = cp_model.CpModel()

# variables definition
x = model.NewIntVar(0, 1000, 'x')
y = model.NewIntVar(0, 1000, 'y')
z = model.NewIntVar(0, 1000, 'z')

# constrains definition
model.Add(2*x+7*y+3*z<=50)
model.Add(3*x-5*y+7*z<=45)
model.Add(5*x+2*y-6*z<=37)
model.Add(x+y+z>=10)

# objective function
# NOTE: si se prefiere optimizar, descomentar esta parte.
#model.Maximize(2*x+2*y+3*z)

#%% LAUNCH SOLVER AND GET RESULTS

# get CP solver
solver = cp_model.CpSolver()
# get results
status = solver.Solve(model)
# display results
print('Status =', solver.StatusName(status))
print('FO =', solver.ObjectiveValue())
print('x =', solver.Value(x))
print('y =', solver.Value(y))
print('z =', solver.Value(z))

# get for all possible solutions 
# NOTE: solo usar esto si la maximizacion del objective function esta comentada.
solution_printer = VarArraySolutionPrinter([x, y, z])
status = solver.SearchForAllSolutions(model, solution_printer)