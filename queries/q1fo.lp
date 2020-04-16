certainty(Z):-r1(X,Y,Z),not p0(X,Z),not p1(x).
p0(X,Z):-r1(X,Y,Z1),r1(X,_,Z),not Z=Z1.
p1(X):-r1(X,Y,Z1),not p2(Y).
p2(Y):-r2(Y,V,W).

certainty(Z) :- not certainty(Z), r1(_,_,Z).

#show certainty/1.
