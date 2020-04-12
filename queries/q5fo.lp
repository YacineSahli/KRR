%q5(z): r1(X,Y,Z), r4(Y,V,W)

%*
certainty(Z) :- r1(X,Y,Z), not d1(Z,X).
d1(Z,X) :- not d2(Z,X,Y,V), r1(X,Y,V).
d2(Z,X,Y,V) :- V=Z, d3(Z,X,Y), r1(X,Y,V).
d3(Z,X,Y) :- r1(X,Y,Z), r4(Y,V,W).
*%

p(X,Z) :- r1(X,Y,Z2), Z2!=Z, r1(X,Y2,Z).
t(X) :- r1(X,Y,Z), not q(Y).
q(Y) :- r4(Y,V,W).
answer(Z) :- r1(X,Y,Z), not p(X,Z), not t(X).

#show answer/1.
