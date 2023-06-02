"""By https://github.com/slavfox"""

from z3 import *
import time


def queens_fox(n):
    start = time.perf_counter()
    sol = Then("simplify", "solve-eqs", "bit-blast", "smt").solver()

    squares = [Bool(f"{i}") for i in range(n * n)]

    # Each row has exactly one queen
    for row in range(n):
        row_squares = [squares[row * n + col] for col in range(n)]
        sol.add(AtMost(*row_squares, 1))
        sol.add(AtLeast(*row_squares, 1))

    # Each column has exactly one queen
    for col in range(n):
        col_squares = [squares[row * n + col] for row in range(n)]
        sol.add(AtMost(*col_squares, 1))
        sol.add(AtLeast(*col_squares, 1))

    # Each diagonal has at most one queen
    for diag in range(2 * n - 1):
        sol.add(
            AtMost(
                *[
                    squares[row * n + col]
                    for row in range(n)
                    for col in range(n)
                    if row + col == diag
                ],
                1,
            )
        )
    for diag in range(-n + 1, n):
        sol.add(
            AtMost(
                *[
                    squares[row * n + col]
                    for row in range(n)
                    for col in range(n)
                    if row - col == diag
                ],
                1,
            )
        )

    print(
        f"Finished building constraints in {time.perf_counter() - start}, {len(sol.assertions())} assertions"
    )
    solve_start = time.perf_counter()
    assert sol.check() == sat, f"Failed to find a solution: {sol.check()}"
    print(f"Solved in {time.perf_counter() - solve_start}")

    mod = sol.model()
    result = [divmod(i, n) for i, square in enumerate(squares) if mod[square]]
    print(result)

    print(f"Total time: {time.perf_counter() - start}")


#for n in [8, 10, 12, 20, 50, 100, 200]:
for n in [100, 200, 400, 800]:
    print(f"\n\nSolving for {n} queens")
    queens_fox(n)
