
certainty(Z,D) :- r1(X,Y,Z), not r_1(Z,D,X), r2(F_0, F_1, D).
r_1(Z,D,X) :- r1(X,Z_0_0,Z_0_1), not r_2(Z,D,X,Z_0_0,Z_0_1), r1(F_0, F_1, Z), r2(F_2, F_3, D).
r_2(Z,D,X,Y,Z_0_1) :- r1(X,Y,Z_0_1), Z_0_1=Z, r_3(Z,D,X,Y).
r_3(Z,D,X,Y) :- r1(X,Y,Z), r3(Y,V), not r_4(Z,D,X,Y), r2(F_0, F_1, D).
r_4(Z,D,X,Y) :- r1(X,Y,Z), r3(Y,Z_1_0), not r_5(Z,D,X,Y,Z_1_0), r2(F_0, F_1, D).
r_5(Z,D,X,Y,V) :- r1(X,Y,Z), r3(Y,V), r2(V,U,D), not r_6(Z,D,X,Y,V).
r_6(Z,D,X,Y,V) :- r1(X,Y,Z), r3(Y,V), r2(V,Z_2_0,Z_2_1), not r_7(Z,D,X,Y,V,Z_2_0,Z_2_1), r3(F_0, D).
r_7(Z,D,X,Y,V,U,Z_2_1) :- r1(X,Y,Z), r3(Y,V), r2(V,U,Z_2_1), Z_2_1=D, r2(F_2, F_3, D).
