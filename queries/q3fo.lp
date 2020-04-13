certainty(Z):-r1(X,Y,Z),r2(V,U,D),not q1(X,Y,Z),not q2(X,Y),not q3(X,Y,D),not q4(X,Y,D).
q1(X,Y,Z):-r1(X,Y,Z1),not Z1=Z,r1(X,Y,Z).
q2(X,Y):-r1(X,Y,Z1),not p2(Y,V),r3(Y,V).
p2(Y,V):-r3(Y,V).
q3(X,Y,D):-r1(X,Y,Z1),p3(D).
p3(Y,D):-r3(Y,V),not p31(V,D),r2(V,U,D).
p31(V,D):-r2(V,U,D).
q4(X,Y,D):-r1(X,Y,Z1),p4(D,Y).
p4(Y,D):-r3(Y,V),p41(V,D).
p41(V,D):-r2(V,U,D1),not D1=D,r2(V,U,D).

#show certainty/1.
