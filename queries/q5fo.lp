p(X,Z) :- r1(X,Y,Z2), Z2!=Z, r1(X,Y2,Z).
t(X) :- r1(X,Y,Z), not q(Y).
q(Y) :- r4(Y,V,W).
cqa(Z) :- r1(X,Y,Z), not p(X,Z), not t(X).

#show cqa/1.
