%q7(z) : r1(X,Y,Z), r2(Y,X,W), r5(X,Y,D)

cqa(Z) :- not d1(Z,Y), r2(Y,X,W), r1(X,Y,Z).
d1(Z,Y) :- not d2(Z,Y,X,W), r2(Y,X,W), r1(X,Y,Z).
d2(Z,Y,X,W) :- not d3(Z,Y,X,W), r2(Y,X,W), r1(X,Y,Z).
d3(Z,Y,X,W) :- r2(Y,X,W), not d4(Z,Y,X,W,P,Q), r1(X,P,Q), r1(X,Y,Z).
d4(Z,Y,X,W,P,Q) :- r1(X,P,Q), P=Y, r2(Y,X,W), Q=Z, d5(Z,Y,X,W).
d5(Z,Y,X,W) :- r5(X,Y,D), not d6(Z,Y,X,W), r2(Y,X,W), r1(X,Y,Z).
d6(Z,Y,X,W) :- not d7(Z,Y,X,W,P,D), r2(Y,X,W), r5(X,P,D), r1(X,Y,Z).
d7(Z,Y,X,W,P,D) :- r2(Y,X,W), r5(X,Z_5_0,D), r1(X,Y,Z), P=Y.

%certainty(Z) :- not certainty(Z), r1(_,_,Z).

#show cqa/1.
