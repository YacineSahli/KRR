import gtmethods
import sys

# q2(z,w) := ∃x, y, v (r1(x | y, z) ∧ r2(y | v, w))

tmp_file = 'bosimfq158plkefvs.lp'
output_file = 'q2gt.lp'

script = """
1 {rr1(X,Y,Z) : r1(X,Y,Z)} 1 :- r1(X,_,_).
1 {rr2(X,Y,Z) : r2(X,Y,Z)} 1 :- r2(X,_,_).
"""

# % rr(X,Y,Z,V,W) :- rr1(X,Y,Z), rr2(Y,V,W).

query = 'q(Z,W) :- r1(X,Y,Z),r2(Y,V,W).\n #show q/2.'


def get_script(var: str):
    # var = 'z,w'
    z, w = var.split(',')
    return script + ':- rr1(_,Y,' + z + '), rr2(Y,_,' + w + ').\n'


if __name__ == "__main__":
    gtmethods.parse_argv(sys.argv, get_script, query, output_file, tmp_file)

