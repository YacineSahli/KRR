certainty :- r1(X,_,_), not p_1(X).
p_1(X) :- r1(X,Y,_), not q_3(Y).
q_3(Y) :- r3(Y,_), not q_2(Y).
q_2(Y) :- r3(Y,V), not q_1(V).
q_1(V) :- r2(V,_,_).

#show certainty/0.