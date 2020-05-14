certainty:-r1(X,Y,Z),not p1(X).
p1(X):-r1(X,Y,Z),not p2(Y).
p2(Y):-r2(Y,V,W).
:-not certainty.

#show certainty/0.