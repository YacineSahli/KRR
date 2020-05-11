certainty(Z):-not certainty(Z),r1(_,_,Z).
certainty(Z):-r1(_,_,Z),q1(X1,Z).
q1(X1,Z):-r2(X1,Y,W),not q2(X1,Z,X,D),r5(X,Y,D),r1(X,Y,Z).
q2(X1,Z,X,D):-r2(X1,Y,W),q4(X,Y,Z,D),r5(X,Y,D),r1(X,Y,Z).
q2(X1,Z,X,D):-r2(X1,Y,W),not q3(Y,Z,W),r5(X,Y,D),r1(X,Y,Z).
q3(Y,Z,W):-r5(X,Y,D),r1(X,Y,Z),r2(_,Y,W).
q4(X,Y,Z,D):-r5(X,Y1,D1),r1(X,Y2,Z1),not Z=Z1,r1(X,Y,Z),r5(X,Y,D).
q4(X,Y,Z,D):-r5(X,Y1,D1),r1(X,Y2,Z1),not Y=Y1,r1(X,Y,Z),r5(X,Y,D).
q4(X,Y,Z,D):-r5(X,Y1,D1),r1(X,Y2,Z1),not Y=Y2,r1(X,Y,Z),r5(X,Y,D).
q4(X,Y,Z,D):-r5(X,Y1,D1),r1(X,Y2,Z1),not D=D1,r1(X,Y,Z),r5(X,Y,D).

#show certainty/1.
