import sys
from db1 import generate


def consistent_tuple(n):
    return 'r1(' + n + ',' + n + ',' + n + ').\n' + 'r4(w' + n + ',1,1).\n' 


def inconsistent_tuple(n, size):
    result = 'r1(' + n + ',' + n + ',' + n + ').\n' + 'r4(w' + n + ',1,1).\n' 
    for i in range(size):
        result += 'r1(' + n + ',p' + str(i+2) + ',p' + n + ').\n' + 'r2(w' + n + ',' + str(i+2) + ',1).\n'
    return result
        
    
def inconsistent_answer(n, yy, zz):
    result = 'r1(' + n + ',' + n + ',' + n + ').\n' \
             + 'r4(' + n + ',1,1).\n' \
             + 'r1(' + n + ',' + yy + ',' + zz + ').\n' \
             + 'r4(' + n + ',1,2).\n'
    return result
    
    
def consistent_answer_1(index):
    x = y = z = v = str(index)
    result = 'r1(' + x + ',' + y + ',' + z + ').\n' \
             + 'r4(' + y + ',1,1).\n' 
    return result
    
    
def consistent_answer_2(index):
    x = y = z = v = str(index)
    yy = 'a'+x
    n = 'm'+x
    result = 'r1(' + x + ',' + y + ',' + z + ').\n' \
         + 'r4(' + y + ',1,1).\n' \
         + 'r1(' + x + ',' + yy + ',' + z + ').\n' \
         + 'r4(' + yy + ',1,1).\n' \
         + 'r4(' + y + ',1,2).\n' \
         + 'r1(' + n + ',' + n + ',' + n + ').\n'
    return result
    
    
if __name__ == "__main__":
    argv = sys.argv[1:]
    assert len(argv) == 4    
    db = generate(2, [float(a) for a in argv], (inconsistent_answer, consistent_answer_1, consistent_answer_2, consistent_tuple, inconsistent_tuple))
    print(db)

