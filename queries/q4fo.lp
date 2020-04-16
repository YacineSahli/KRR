%%%
% Query from Dixit & Kolaitis.
% q4(z,d) := R1(x,y,z) AND R3(y,v) AND R2(v,u,d)
% Note that d is a free variable!!!
%%%

%%% The following rule is optional.
cqa(Z,D) :- not cqa(Z,D), r_1(_,_,Z), r_2(_,_,D).
%%%
cqa(Z,D) :- r_1(X,_,Z), not p_0(X,Z), not p_1(X), r_2(V,_,D).
p_0(X,Z) :- r_1(X,_,W), W != Z, r_1(_,_,Z).
p_1(X) :- r_1(X,Y,_), not q_3(Y).
q_3(Y) :- r_3(Y,_), not q_2(Y).
q_2(Y) :- r_3(Y,V), not q_1(V).
q_1(V) :- r_2(V,_,_), not q_0(V).
q_0(V) :- r_2(V,_,W), W != D, r_2(_,_,D).

#show cqa/2.

