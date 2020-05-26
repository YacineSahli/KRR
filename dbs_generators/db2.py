import sys
from generate_method import generate


def consistent_tuple(n):
    return 'r1(' + n + ',' + n + ',' + n + ').\n' + 'r2(w' + n + ',1,w' + n + ').\n' 


def inconsistent_tuple(n):
    result = 'r1(' + n + ',' + n + ',' + n + ').\n' + 'r2(w' + n + ',1,w' + n + ').\n' \
             + 'r1(' + n + ',p' + n + ',p' + n + ').\n' + 'r2(w' + n + ',2,w' + n + ').\n'
    return result

    
def inconsistent_answer(n, yy, zz):
    x = y = z = w = n
    result = 'r1(' + x + ',' + y + ',' + z + ').\n' \
             + 'r2(' + y + ',1,' + w + ').\n' \
             + 'r1(' + x + ',' + yy + ',' + zz + ').\n' \
             + 'r2(' + y + ',2,' + w + ').\n'
    return result
    
    
def consistent_answer_1(index):
    x = y = z = w = str(index)
    result = 'r1(' + x + ',' + y + ',' + z + ').\n' \
             + 'r2(' + y + ',1,' + w +').\n' 
    return result
    
    
def consistent_answer_2(index):
    x = y = z = w = str(index)
    yy = 'a'+x
    o = 'm'+x
    result = 'r1(' + x + ',' + y + ',' + z + ').\n' \
             + 'r2(' + y + ',1,' + w +').\n' \
             + 'r1(' + x + ',' + yy + ',' + z + ').\n' \
             + 'r2(' + yy + ',1,' + w +').\n' \
             + 'r1(' + o + ',' + o + ',' + o + ').\n' \
             + 'r2(' + y + ',2,' + w +').\n' 
    return result
    
    
if __name__ == "__main__":
    argv = sys.argv[1:]
    assert len(argv) == 4    
    db = generate(2, [float(a) for a in argv], (inconsistent_answer, consistent_answer_1, consistent_answer_2, consistent_tuple, inconsistent_tuple))
    print(db)
    

