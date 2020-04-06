
%q1(z) := ∃x, y, v, w (R1(x, y, z) ∧ R2(y, v, w))


%rr1 for repaired r1
1 {rr1(X,Y,Z) : r1(X,Y,Z)} 1 :- r1(X,_,_).

1 {rr2(X,Y,Z) : r2(X,Y,Z)} 1 :- r2(X,_,_).

1 {rr3(X,Y) : r3(X,Y)} 1 :- r3(X,_).

:- rr1(X,Y,Z), rr2(Y,V,W).



