%q= ∃x, y, z, v, w (R 1 (x| y, z) ∧ R 4 (y| v, "w"))

q1:-r1(X,Y,Z),not p1(X).
p1(X):-r1(X,Y,Z),not p2(Y).
p2(Y):-r4(Y,V,W),W==w.

certainty:-q1.
certainty:-not certainty.

#show certainty/0.