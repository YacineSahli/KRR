%q5(z): r1(X,Y,Z), r4(Y,V,W)

1 {rr1(X,Y,Z) : r1(X,Y,Z)} 1 :- r1(X,_,_).
1 {rr4(X,Y,Z) : r4(X,Y,Z)} 1 :- r4(X,Y,_).

:- rr1(X,Y,Z), rr4(Y,V,W). 

