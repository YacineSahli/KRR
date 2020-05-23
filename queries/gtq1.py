import gtmethods
import sys

# q1(z) := ∃x, y, v, w (R1(x | y, z) ∧ R2(y | v, w))

tmp_file = 'bosimfq15846ebaefvs.lp'
output_file = 'q1gt.lp'

script = """
1 {rr1(X,Y,Z) : r1(X,Y,Z)} 1 :- r1(X,_,_).
1 {rr2(X,Y,Z) : r2(X,Y,Z)} 1 :- r2(X,_,_).
"""

# % rr(X,Y,Z,V,W) :- rr1(X,Y,Z), rr2(Y,V,W).

query = 'q(Z) :- r1(_,Y,Z), r2(Y,_,_).\n #show q/1.'


def get_script(var: str):
    return script + ':- rr1(_,Y,' + var + '), rr2(Y,_,_).\n'


if __name__ == "__main__":
    gtmethods.parse_argv(sys.argv, get_script, query, output_file, tmp_file)

