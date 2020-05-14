%q=∃x, y, z, v, w (R 1 (x, y, z) ∧ R 2 (y, v, w))

1{rr1(X,Y,Z):r1(X,Y,Z)}1:-r1(X,_,_).
1{rr2(X,Y,Z):r2(X,Y,Z)}1:-r2(X,_,_).
:-rr1(X,Y,Z),rr2(Y,V,W).