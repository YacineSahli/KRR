%q5(z): r1(X,Y,Z), r4(Y,V,W)

certainty(Z) :- r1(X,Y,Z), not d1(Z,X).
d1(Z,X) :- not d2(Z,X,Y,V), r1(X,Y,V).
d2(Z,X,Y,V) :- V=Z, d3(Z,X,Y), r1(X,Y,V).
d3(Z,X,Y) :- r1(X,Y,Z), r4(Y,V,W).


