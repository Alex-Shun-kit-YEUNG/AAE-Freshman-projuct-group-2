# import the solver
from ortools.linear_solver import pywraplp
solver = pywraplp.solver.CreateSolver('SCIP')

variables = [[]] * len(unknowns)
