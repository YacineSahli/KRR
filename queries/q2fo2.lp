certainty(W,Z):-r1(X,Y,Z),r2(Y,V,W),not p0(Z,X),not q0(W,X).
p0(Z,X):-r1(X,Y,Z1),not Z1=Z,r1(X,_,Z).
q0(W,X):-r1(X,Y,Z1),not q1(W,Y),r2(Y,V,W).
q1(W,Y):-r2(Y,V,W),not q2(W,Y).
q2(W,Y):-r2(Y,V,W1),not W1=W,r2(Y,_,W).

#show certainty/2.
