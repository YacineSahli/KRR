import gtmethods
import sys

# q6(z) := ∃x, y, m, w, d (r1(x| y, z) and r2(m| y, w) and r5(x| y, d))

tmp_file = 'bosi484m8444baefvs.lp'
output_file = 'q6gt.lp'

script = """
1 {rr1(X,Y,Z) : r1(X,Y,Z)} 1 :- r1(X,_,_).
1 {rr2(X,Y,Z) : r2(X,Y,Z)} 1 :- r2(X,_,_).
1 {rr5(X,Y,Z) : r5(X,Y,Z)} 1 :- r5(X,_,_).
"""

query = 'q(Z) :- r1(X,Y,Z), r2(_,Y,_), r2(X,Y,_).\n #show q/1.'


def get_script(var: str):
    return script + ':- rr1(X,Y,' + var + '), rr2(_,Y,_), rr5(X,Y,_).\n'


if __name__ == "__main__":
    gtmethods.parse_argv(sys.argv, get_script, query, output_file, tmp_file)
        
