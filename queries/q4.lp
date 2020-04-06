%q4(z,d) := ∃x, y, v, u (R1 (x, y, z) ∧ R3 (y, v) ∧ R2 (v, u, d))

1 {rr1(X,Y,Z) : r1(X,Y,Z)} 1 :- r1(X,_,_).

1 {rr2(X,Y,Z) : r2(X,Y,Z)} 1 :- r2(X,_,_).

1 {rr3(X,Y) : r3(X,Y)} 1 :- r3(X,_).

:- rr1(X,Y,Z), rr2(V,U,D), rr3(Y,V). 

