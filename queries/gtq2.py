import execute_query
import sys

# q2(z,w) := ∃x, y, v (r1(x | y, z) ∧ r2(y | v, w))

tmp_file = 'q2gt.lp'

script = """
1 {rr1(X,Y,Z) : r1(X,Y,Z)} 1 :- r1(X,_,_).
1 {rr2(X,Y,Z) : r2(X,Y,Z)} 1 :- r2(X,_,_).
"""

rr = 'rr(Z,W) :- rr1(X,Y,Z), rr2(Y,V,W).\n'

query = 'q(Z,W) :- r1(X,Y,Z),r2(Y,V,W).\n #show q/2.'


def get_script(var: str, rr_b=False):
    # var = 'z,w'
    if rr_b:
        return script + rr
    z, w = var.split(',')
    return script + ':- rr1(_,Y,' + z + '), rr2(Y,_,' + w + ').\n'


if __name__ == "__main__":
    execute_query.parse_argv(sys.argv, get_script, query, tmp_file)

