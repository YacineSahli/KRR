q1:-r1(X,Y,Z),not p1(X).
p1(X):-r1(X,Y,Z),not p2(Y).
p2(Y):-r2(Y,V,W).

certainty:-q1.
certainty:-not certainty.

#show certainty/0.