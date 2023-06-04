% Found under https://www.scryer.pl/clpz.html

% For SWI-Prolog

:- [library(clpfd)].

n_queens(N, Qs) :-
        length(Qs, N),
        Qs ins 1..N,
        safe_queens(Qs).

safe_queens([]).
safe_queens([Q|Qs]) :- safe_queens(Qs, Q, 1), safe_queens(Qs).

safe_queens([], _, _).
safe_queens([Q|Qs], Q0, D0) :-
        Q0 #\= Q,
        Q0 - Q #\= D0,
        Q - Q0 #\= D0,
        D1 #= D0 + 1,
        safe_queens(Qs, Q0, D1).

% ?- time((n_queens(90, Qs), labeling([ff], Qs))).
% % 5,695,631 inferences, 0.318 CPU in 0.318 seconds (100% CPU, 17932872 Lips)
% Qs = [1, 3, 5, 50, 42, 4, 49, 7, 59|...] .
