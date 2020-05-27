cqa(Z):-r1(X,Y,Z),not p0(X,Z),not p1(X).
p0(X,Z):-r1(X,Y,Z1), Z!=Z1, r1(X,_,Z).
p1(X):-r1(X,Y,Z1),not p2(Y).
p2(Y):-r2(Y,V,W).

#show cqa/1.
