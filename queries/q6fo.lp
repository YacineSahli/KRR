%q6(z) : r1(X,Y,Z), r2(V,Y,W), r5(X,Y,D)

d1(Z,V) :- not d2(Z,V,Y,W), r2(V,Y,W).
d2(Z,V,Y,W) :- r1(X,Y,Z), not d3(Z,V,Y,W,X), r2(V,Y,W).
d3(Z,V,Y,W,X) :- r1(X,P,Q), not d4(Z,V,Y,W,X,P,Q), r2(V,Y,W).
d4(Z,V,Y,W,X,P,Q) :- d5(Z,V,Y,W,X), Q=Z, r2(V,Y,W), P=Y, r1(X,P,Q).
d5(Z,V,Y,W,X) :- r5(X,Y,D), not d6(Z,V,Y,W,X), r1(X,Y,Z), r2(V,Y,W).
d6(Z,V,Y,W,X) :- r5(X,Z_5_0,D), not d7(Z,V,Y,W,X,Z_5_0,D), r1(X,Y,Z), r2(V,Y,W).
d7(Z,V,Y,W,X,P,D) :- r5(X,P,D), r1(X,Y,Z), P=Y, S(V,Y,W).

