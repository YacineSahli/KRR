import sys
from db3 import generate

        
def consistent_tuple(n):
    return 'r1(' + n + ',' + n + ',' + n + ').\n' + 'r2(w' + n + ',1,1).\n' + 'r3(q' + n + ',q' + n + ').\n'

    
def inconsistent_tuple(n, size):
    result = 'r1(' + n + ',' + n + ',' + n + ').\n' + 'r2(w' + n + ',1,1).\n' + 'r3(' + n + ',' + n + ').\n'
    for i in range(size):
        result += 'r1(' + n + ',p' + n + ',p' + str(i+1) + ').\n' + 'r2(w' + n + ',1,' + str(i+2) + ').\n' + 'r3(' + n + ',m' + str(i+2) + ').\n'
    return result   
    
    
def inconsistent_answer(n, yy, zz):
    x = y = z = d = v = n
    o = 'o' + x
    k = 'k' + x
    m = 'm' + x
    result = 'r1(' + x + ',' + y + ',' + z + ').\n' \
             + 'r3(' + y + ',' + v + ').\n' \
             + 'r2(' + v + ',1,' + d + ').\n' \
             + 'r1(' + x + ',' + yy + ',' + zz + ').\n' \
             + 'r3(' + y + ',o' + k + ').\n' \
             + 'r2(' + k + ',1,' + d + ').\n' \
             + 'r1(' + o + ',' + o + ',' + o + ').\n' \
             + 'r3(' + m + ',o' + m + ').\n'\
             + 'r2(' + k + ',2,' + d + ').\n'
    return result
    
def consistent_answer_1(index):
    x = y = z = v = d = str(index)
    result = 'r1(' + x + ',' + y + ',' + z + ').\n' \
             + 'r3(' + y + ',' + v + ').\n'\
             + 'r2(' + v + ',1,' + d + ').\n' 
    return result
    
    
def consistent_answer_2(index):
    x = y = z = v = d = str(index)
    yy = 'yy' + x
    o = 'o' + x
    p = 'p' + x
    result = 'r1(' + x + ',' + y + ',' + z + ').\n' \
             + 'r3(' + y + ',' + v + ').\n'\
             + 'r2(' + v + ',1,' + d + ').\n' \
             + 'r1(' + x + ',' + yy + ',' + z + ').\n' \
             + 'r3(' + yy + ',' + v + ').\n'\
             + 'r2(' + v + ',2,' + d + ').\n' \
             + 'r1(' + o + ',' + o + ',' + o + ').\n' \
             + 'r3(' + yy + ',' + p + ').\n' \
             + 'r2(' + p + ',1,' + d + ').\n' 
    return result
    
    
if __name__ == "__main__":
    argv = sys.argv[1:]
    assert len(argv) == 4    
    db = generate(3, [float(a) for a in argv], (inconsistent_answer, consistent_answer_1, consistent_answer_2, consistent_tuple, inconsistent_tuple))
    print(db)
    

