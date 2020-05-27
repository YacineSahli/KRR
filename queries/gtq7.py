import execute_query
import sys

# q7(z) := ∃x, y, w, d (r1(x| y, z) and r2(y| x, w) and r5(x| y, d))

tmp_file = 'q7gt.lp'

script = """
1 {rr1(X,Y,Z) : r1(X,Y,Z)} 1 :- r1(X,_,_).
1 {rr2(X,Y,Z) : r2(X,Y,Z)} 1 :- r2(X,_,_).
1 {rr5(X,Y,Z) : r5(X,Y,Z)} 1 :- r5(X,_,_).
"""

query = 'q(Z) :- r1(X,Y,Z), r2(Y,X,_), r2(X,Y,_).\n #show q/1.'


def get_script(var: str):
    return script + ':- rr1(X,Y,' + var + '), rr2(Y,X,_), rr5(X,Y,_).\n'


if __name__ == "__main__":
    execute_query.parse_argv(sys.argv, get_script, query, tmp_file)
        
