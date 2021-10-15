import numpy as np
from sympy import symbols, Eq, solve

T, F = symbols('T, F')

eq1 = Eq(T - F <= 30)
eq2 = Eq(-0.5*T - F <= -30)
eq3 = Eq(2*T - F >= 20)
eq4 = Eq(-4*T - F >= -220)

solve((eq1, eq2, eq3, eq4), (T, F))

sol_dict = solve((eq1, eq2, eq3, eq4), (T, F))
print(f'T = {sol_dict[T]}')
print(f'F = {sol_dict[F]}')