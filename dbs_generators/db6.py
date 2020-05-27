import sys


def generate(arity, parameters, methods):
    
    size, inconsistence, nb_consist_answers, nb_inconsistent_answers = parameters
    inconsistent_answer, consistent_answer_1, consistent_tuple, inconsistent_tuple = methods
    
    nb_inconsistent_answers = int(nb_inconsistent_answers)
    nb_consist_answers = int(nb_consist_answers)
    nb_tuples = int(size/arity)
    remaining_inconsistent_tuples = int(inconsistence * nb_tuples)  # nb tuples to remove to have a consistent db
    answer = ""
    
    assert nb_inconsistent_answers <= remaining_inconsistent_tuples
    
    total_tuples = 0  # Nb tuples for one relation 
    i = 0
    while i < nb_inconsistent_answers:
        n = yy = zz = str(i)
        if i % 2 == 0 and nb_inconsistent_answers - i > 2:  # another_z
            zz = 'z' + n
            i += 2 # Another_z pattern add two inconsistant answers
        else:  # dangling
            yy = 'y' + n
            i += 1 
        total_tuples += 2   
        remaining_inconsistent_tuples -= 1  # For every inconsistent answer, a broken primary key was added 
        answer += inconsistent_answer(n, yy, zz)
    
    start = total_tuples
    
    # print('TEST0 : ', total_tuples, answer.count('r1'), answer.count('r2'))
    
    for _ in range(nb_consist_answers):
        answer += consistent_answer_1(total_tuples)
        total_tuples += 1
    
    # print('TEST1 : ', total_tuples, answer.count('r1'), answer.count('r2'))    
    
    while remaining_inconsistent_tuples > 0:
        n = str(total_tuples)
        answer += inconsistent_tuple(n)
        total_tuples += 2
        remaining_inconsistent_tuples -= 1
        
    # print('TEST2 : ', total_tuples, answer.count('r1'), answer.count('r2'))
            
    while total_tuples < nb_tuples:
        n = str(total_tuples)
        answer += consistent_tuple(n)
        total_tuples += 1
    
    # print('TEST3 : ', total_tuples, answer.count('r1'), answer.count('r2'))
    
    return answer

def consistent_tuple(n):
    return 'r1(' + n + ',' + n + ',' + n + ').\n' + 'r2(p' + n + ',p' + n + ',1).\n' + 'r5(q' + n + ',q' + n + ',1).\n'


def inconsistent_tuple(n):
    result = 'r1(' + n + ',' + n + ',' + n + ').\n' + 'r2(p' + n + ',p' + n + ',1).\n' + 'r5(q' + n + ',q' + n + ',1).\n' \
             + 'r1(' + n + ',' + n + ',l' + n + ').\n' + 'r2(p' + n + ',p' + n + ',2).\n' + 'r5(q' + n + ',q' + n + ',2).\n'
    return result

    
def inconsistent_answer(n, yy, zz):
    result = 'r1(' + n + ',' + n + ',' + n + ').\n' \
             + 'r2(' + n + ',' + n + ',1).\n' \
             + 'r5(' + n + ',' + n + ',1).\n'\
             + 'r1(' + n + ',' + yy + ',' + zz + ').\n' \
             + 'r2(' + n + ',' + n + ',2).\n' \
             + 'r5(' + n + ',' + n + ',2).\n'
    return result
    
    
def consistent_answer_1(index):
    x = y = z = m = str(index)
    result = 'r1(' + x + ',' + y + ',' + z + ').\n' \
             + 'r2(' + m + ',' + y + ',1).\n' \
             + 'r5(' + x + ',' + y + ',1).\n'
    return result
    
    
if __name__ == "__main__":
    argv = sys.argv[1:]
    assert len(argv) == 4    
    db = generate(3, [float(a) for a in argv], (inconsistent_answer, consistent_answer_1, consistent_tuple, inconsistent_tuple))
    print(db)
    
