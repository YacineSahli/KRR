%q5(z) := ∃x, y, v, w (R 1 (x, y, z) ∧ R 4 (y, v, w))

p0(Z):-r1(X,Y,Z),not p1(Z,X).
p1(Z,X):-r1(X,Y,Z),r1(X,V1,V2),not p2(Z,X,V1,V2).
p2(Z,X,V1,V2):-r1(X,Y,Z),r1(X,V1,V2),d0(Z,Y),V1=Y,V2=Z.

d0(Z,Y):-r4(Y,V,W),not d1(Z,Y,V).
d1(Z,Y,V):-r4(Y,V,W),r4(Y,V,V1),not d2(Z,Y,V,W,V1).
d2(Z,Y,V,W,V1):-r4(Y,V,W),r4(Y,V,V1),V1=W.
