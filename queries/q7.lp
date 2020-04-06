P0(Z):-R1(X,Y,Z),not P1(Z,X,Y).
P1(Z,X,Y):-R1(X,Y,Z),R1(X,V1,V2),not P2(Z,X,Y,V1,V2).
P2(Z,X,Y,V1,V2):-R1(X,Y,Z),R1(X,V1,V2),V1=Y,V2=Z,D0(X,Y).

D0(X,Y):-R2(Y,X,W),not D1(X,Y).
D1(X,Y):-R2(Y,X,W),R2(Y,V1,V2),not D2(X,Y,W,V1,V2).
D2(X,Y,W,V1,V2):-R2(Y,X,W),R2(Y,V1,V2),V1=X,V2=W,F0(X,Y).

F0(X,Y):-R5(X,Y,D),not F1(X,Y).
F1(X,Y):-R5(X,Y,D),R5(X,V1,V2),not F2(X,Y,D,V1,V2).
F2(X,Y,D,V1,V2):-R5(X,Y,D),R5(X,V1,V2),V1=Y,V2=D.
