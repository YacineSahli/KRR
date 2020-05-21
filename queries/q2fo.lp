certainty(W,Z):-r1(X,Y,Z),not p0(Z,X),not q0(W,X), r2(P,Q,W).
p0(Z,X):-r1(X,Y,Z1),not Z1=Z,r1(X,_,Z).
q0(W,X):-r1(X,Y,Z1),not q1(W,Y), r2(P,Q,W).
q1(W,Y):-r2(Y,V,W),not q2(W,Y).
q2(W,Y):-r2(Y,V,W1),not W1=W,r2(Y,_,W).

certainty(W,Z) :- not certainty(W,Z), r1(_,_,Z), r2(_,_,W).

#show .
