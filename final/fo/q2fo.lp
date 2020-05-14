certainty :- r1(X,_,_), not p1(X).
p1(X) :- r1(X,Y,_), not q3(Y).
q3(Y) :- r3(Y,_), not q2(Y).
q2(Y) :- r3(Y,V), not q1(V).
q1(V) :- r2(V,_,_).
:-not certainty.

#show certainty/0.