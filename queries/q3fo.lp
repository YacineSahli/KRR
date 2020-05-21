%%%
% Query from Dixit & Kolaitis.
% q3(z) := R1(x,y,z) AND R3(y,v) AND R2(v,u,d)
% Note that d is a bound variable!!!
% R1->R3->R2
%%%

%%% The following rule is optional.
cqa(Z) :- not cqa(Z), r1(_,_,Z).
%%%
cqa(Z) :- r1(X,_,Z), not p_0(X,Z), not p_1(X).
p_0(X,Z) :- r1(X,_,W), W != Z, r1(_,_,Z).
p_1(X) :- r1(X,Y,_), not q_3(Y).
q_3(Y) :- r3(Y,_), not q_2(Y).
q_2(Y) :- r3(Y,V), not q_1(V).
q_1(V) :- r2(V,_,_).

#show .

