%q5(z): r1(X,Y,Z), r4(Y,V,W)

p(X,Z) :- r1(X,Y,Z2), Z2!=Z, r1(X,Y2,Z).
t(X) :- r1(X,Y,Z), not q(Y).
q(Y) :- r4(Y,V,W).
answer(Z) :- r1(X,Y,Z), not p(X,Z), not t(X).

answer(Z) :- not answer(Z), r1(_,_,Z).

#show .
