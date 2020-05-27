import execute_query
import sys

# q5(z) := ∃x, y, v, w (r1(x| y, z) and r4(y, v| w))

tmp_file = 'q5gt.lp'


script = """
1 {rr1(X,Y,Z) : r1(X,Y,Z)} 1 :- r1(X,_,_).
1 {rr4(X,Y,Z) : r4(X,Y,Z)} 1 :- r4(X,Y,_).
"""

rr = 'rr(Z) :- rr1(X,Y,Z), rr4(Y,V,W).\n'

query = 'q(Z) :- r1(_,Y,Z), r4(Y,_,_).\n #show q/1.'


def get_script(var: str, rr_b=False):
    if rr_b:
        return script + rr
    return script + ':- rr1(_,Y,' + var + '), rr4(Y,_,_).\n'


if __name__ == "__main__":
    execute_query.parse_argv(sys.argv, get_script, query, tmp_file)
        
