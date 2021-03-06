import execute_query
import sys

# q4(z, d) := ∃x, y, v, u (r1(x| y, z) and r3(y| v) and r2(v| u, d))

tmp_file = 'q4gt.lp'

script = """
1 {rr1(X,Y,Z) : r1(X,Y,Z)} 1 :- r1(X,_,_).
1 {rr2(X,Y,Z) : r2(X,Y,Z)} 1 :- r2(X,_,_).
1 {rr3(X,Y) : r3(X,Y)} 1 :- r3(X,_).
"""

rr = 'rr(Z,D) :- rr1(X,Y,Z), rr3(Y,V), rr2(V,U,D).\n'

query = 'q(Z,D) :- r1(X,Y,Z), r3(Y,V), r2(V,U,D).\n #show q/2.'


def get_script(var: str, rr_b=False):
    if rr_b:
        return script + rr
    z, d = var.split(',')
    return script + ':- rr1(X,Y,' + z + '), rr3(Y,V), rr2(V,_,' + d + ').\n'


if __name__ == "__main__":
    execute_query.parse_argv(sys.argv, get_script, query, tmp_file)

