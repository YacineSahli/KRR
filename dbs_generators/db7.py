import sys
from db6 import generate


def consistent_tuple(n):
    return 'r1(' + n + ',' + n + ',' + n + ').\n' + 'r2(p' + n + ',p' + n + ',1).\n' + 'r5(q' + n + ',q' + n + ',1).\n'


def inconsistent_tuple(n, size):
    result = 'r1(' + n + ',' + n + ',' + n + ').\n' + 'r2(p' + n + ',p' + n + ',1).\n' + 'r5(q' + n + ',q' + n + ',1).\n'
    for i in range(size):
        result += 'r1(' + n + ',' + n + ',l' + str(i+1) + ').\n' + 'r2(p' + n + ',p' + str(i+1) + ',2).\n' + 'r5(q' + n + ',q' + n + ',' + str(i+1) + ').\n'
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
    
    
if __name__ == "__main__":
    argv = sys.argv[1:]
    assert len(argv) == 4    
    db = generate(3, [float(a) for a in argv], (inconsistent_answer, consistent_answer_1, consistent_tuple, inconsistent_tuple))
    print(db)
    
