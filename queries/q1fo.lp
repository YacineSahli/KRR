
%q1(z) := ∃x, y, v, w (R1(x, y, z) ∧ R2(y, v, w))

p0(Z) :- r1(X,Y,Z), not p1(Z,X).
p1(Z,X) :- r1(X,Y,Z), r1(X,V1,V2), not p2(Z,X,V1,V2).
p2(Z,X,V1,V2) :- r1(X,Y,Z), r1(X,V1,V2), d0(Y), V1=Y, V2=Z.

d0(Y) :- r2(Y,V,W), not d1(Z,Y).
d1(Z,Y) :- r2(Y,V,W), r2(Y,V1,V2), not d2(Z,Y,V1,V2).
d2(Z,Y,V1,V2) :- r2(


F0(X,Y):-R5(X,Y,D),not F1(X,Y).
F1(X,Y):-R5(X,Y,D),R5(X,V1,V2),not F2(X,Y,D,V1,V2).
F2(X,Y,D,V1,V2):-R5(X,Y,D),R5(X,V1,V2),V1=Y,V2=D.

