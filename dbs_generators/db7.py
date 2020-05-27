import sys
from generate_method import generate


def consistent_tuple(n):
    return 'r1(' + n + ',' + n + ',' + n + ').\n' + 'r2(p' + n + ',p' + n + ',1).\n' + 'r5(q' + n + ',q' + n + ',1).\n'


def inconsistent_tuple(n):
    result = 'r1(' + n + ',' + n + ',' + n + ').\n' + 'r2(p' + n + ',p' + n + ',1).\n' + 'r5(q' + n + ',q' + n + ',1).\n' \
             + 'r1(' + n + ',' + n + ',l' + n + ').\n' + 'r2(p' + n + ',p' + n + ',2).\n' + 'r5(q' + n + ',q' + n + ',2).\n'
    return result

    
def inconsistent_answer(n, yy, zz):
    x = y = z = n
    result = 'r1(' + x + ',' + y + ',' + z + ').\n' \
             + 'r2(' + y + ',' + x + ',1).\n' \
             + 'r5(' + x + ',' + y + ',1).\n'\
             + 'r1(' + x + ',' + yy + ',' + zz + ').\n' \
             + 'r2(' + y + ',' + x + ',2).\n' \
             + 'r5(' + x + ',' + y + ',2).\n'
    return result
    
    
def consistent_answer_1(index):
    x = y = z = v = str(index)
    result = 'r1(' + x + ',' + y + ',' + z + ').\n' \
             + 'r2(' + y + ',' + x + ',1).\n' \
             + 'r5(' + x + ',' + y + ',1).\n'
    return result
    
    
def consistent_answer_2(index):
    x = y = z = v = str(index)
    yy = 'a'+x
    o = 'o'+x
    result = 'r1(' + x + ',' + y + ',' + z + ').\n' \
             + 'r2(' + y + ',' + x + ',1).\n' \
             + 'r5(' + x + ',' + y + ',1).\n' \
             + 'r1(' + x + ',' + yy + ',' + z + ').\n' \
             + 'r2(' + yy + ',' + x + ',1).\n' \
             + 'r5(' + x + ',' + yy + ',1).\n' \
             + 'r1(' + o + ',' + o + ',' + o + ').\n' \
             + 'r2(' + yy + ',' + x + ',2).\n' \
             + 'r5(' + o + ',' + o + ',1).\n' 
    return result
    
    
if __name__ == "__main__":
    argv = sys.argv[1:]
    assert len(argv) == 4    
    db = generate(3, [float(a) for a in argv], (inconsistent_answer, consistent_answer_1, consistent_answer_2, consistent_tuple, inconsistent_tuple))
    print(db)
    
