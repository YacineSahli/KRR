%q=E x : r1(x,y) et r2(y,x)

1{rr1(X,Y):r1(X,Y)}1:-r1(X,_).
1{rr2(X,Y):r2(X,Y)}1:-r2(X,_).
:-rr1(X,Y),rr2(Y,X).
