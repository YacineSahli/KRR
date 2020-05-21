import os
import sys

tmp_file = 'bosimfq15846ebaefvs.lp'
output_file = 'q1gt.lp'

script = """
%q1(z) := ∃x, y, v, w (R1(x | y, z) ∧ R2(y | v, w))


%rr1 for repaired r1
1 {rr1(X,Y,Z) : r1(X,Y,Z)} 1 :- r1(X,_,_).
1 {rr2(X,Y,Z) : r2(X,Y,Z)} 1 :- r2(X,_,_).

rr(X,Y,Z,V,W) :- rr1(X,Y,Z), rr2(Y,V,W).

"""

def build_rr_line(s :str):
    array = s.replace('q(','').replace(')','').strip('\n').split(' ')
    res = ':- '
    for var in array:
        res += 'rr(_,_,' + var + ',_,_), '
    return res[:-2] + '.\n'
    
def write_lp_file(s: str):
    rr_line = build_rr_line(s)
    f = open(output_file, "w")
    f.write(script)
    f.write(rr_line)
    f.close()
    
def write_tmp_file():
    f = open(tmp_file, "w")
    f.write('q(Z) :- r1(_,_,Z).\n #show q/1.')
    f.close()

def rm_tmp_file():
    cmd = 'rm ' + tmp_file
    os.system(cmd)

if __name__ == "__main__":
    
    if len(sys.argv) != 2:
        print('Input file path expected as argument')
    else:
        write_tmp_file()
        cmd = 'clingo ' + sys.argv[1] + ' ' + tmp_file
        stream = os.popen(cmd)
        output = stream.readlines()
        write_lp_file(output[4])
        rm_tmp_file()
        
