#!/usr/bin/python -u
# -*- coding: latin-1 -*-
# 
# n-queens in Z3
#
# Alternative formulation compared to nqueen.py
# Slower.
# 
# This Z3 model was written by Hakan Kjellerstrand (hakank@gmail.com)
# See also my Z3 page: http://hakank.org/z3/
# 
# 
from z3 import *
import time

def queens(n, need_solutions = 1):
    sol = SolverFor("QF_FD")

    q = IntVector("q", n) # this is much faster # n=100: 17.1s

    # Domains
    sol.add([And(q[i]>=0, q[i] <= n-1) for i in range(n)])

    # Constraints
    for i in range(n):
        for j in range(i):
            sol.add(q[i] != q[j], q[i]-q[j] != i-j, q[i]-q[j] != j-i)

    # Show all solutions
    num_solutions = 0
    start = time.time()
    while num_solutions < need_solutions and sol.check() == sat:
        m = sol.model()
        ss = [m.evaluate(q[i]) for i in range(n)]
        sol.add( Or([q[i] != ss[i] for i in range(n)]) )
        print("q=",ss)
        num_solutions = num_solutions + 1

    print("num_solutions:", num_solutions)
    end = time.time()
    value = end - start
    print("Time: ", value)


#for n in [8,10,12,20,50,100,200]:
for n in [100,200,400,800]:
    print("Testing ", n)
    queens(n, 1)

# Show all 92 solutions
# queens(8,1)    

