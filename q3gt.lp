%q3(z):=E x, y, v, u, d | r1(x | y, z) et r3(y | v) et r2(v | u, d)

1{rr1(X,Y,Z):r1(X,Y,Z)}1:-r1(X,_,_).
1{rr3(Y,V):r3(Y,V)}1:-r3(Y,_).
1{rr2(V,U,D):r2(V,U,D)}1:-r2(V,_,_).
:-rr1(X,Y,Z),rr3(Y,V),rr2(V,U,D).
