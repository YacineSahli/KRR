%q6(z):=∃ x, y, x', w, d (R1(x| y, z) ∧ R2(x'| y, w) ∧ R5(x| y, d))

1{rr1(X,Y,Z):r1(X,Y,Z)}1:-r1(X,_,Z).
1{rr2(XX,Y,W):r2(XX,Y,W)}1:-r2(XX,_,_).
1{rr5(X,Y,D):r5(X,Y,D)}1:-r5(X,_,_).
:-rr1(X,Y,Z),rr2(XX,Y,_),rr5(X,Y,_).
