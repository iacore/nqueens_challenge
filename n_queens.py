# I forgot where I got this

from z3 import *

def queens(n):
    Q = [Int('Q_%i' % (i + 1)) for i in range(n)]

    val_c  = [And(1 <= Q[i], Q[i] <= n) for i in range(n)]
    col_c  = [Distinct(Q)]
    diag_c = [If(i == j, True, And(Q[i] - Q[j] != i - j, Q[i] - Q[j] != j - i)) for i in range(n) for j in range(i)]

    sol = Solver()
    sol.add(val_c + col_c + diag_c)

    num_solutions = 0

    while sol.check() == sat:
        mod = sol.model()
        ss = [mod.evaluate(Q[i]) for i in range(n)]
        print(ss)
        num_solutions += 1
        sol.add(Or([Q[i] != ss[i] for i in range(n)]))

    print("num_solutions:", num_solutions)

queens(4)
queens(8)
queens(90)
