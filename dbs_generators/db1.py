import sys

def generate(arity, parameters, methods):
    
    size, inconsistence, nb_consist_answers, nb_inconsistent_answers = parameters
    inconsistent_answer, consistent_answer_1, consistent_answer_2, consistent_tuple, inconsistent_tuple = methods
    
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
    
    for i in range(start, start + nb_consist_answers):
        if remaining_inconsistent_tuples > 0 and i % 2 == 0:
            answer += consistent_answer_2(i)
            remaining_inconsistent_tuples -= 1
            total_tuples += 2
        else:
            answer += consistent_answer_1(i)
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
    return 'r1(' + n + ',' + n + ',' + n + ').\n' + 'r2(w' + n + ',1,1).\n' 


def inconsistent_tuple(n):
    result = 'r1(' + n + ',' + n + ',' + n + ').\n' + 'r2(w' + n + ',1,1).\n' \
             + 'r1(' + n + ',p' + n + ',p' + n + ').\n' + 'r2(w' + n + ',2,1).\n'
    return result

    
def inconsistent_answer(n, yy, zz):
    result = 'r1(' + n + ',' + n + ',' + n + ').\n' \
             + 'r2(' + n + ',1,1).\n' \
             + 'r1(' + n + ',' + yy + ',' + zz + ').\n' \
             + 'r2(' + n + ',1,2).\n'
    return result
    
    
def consistent_answer_1(index):
    x = y = z = str(index)
    result = 'r1(' + x + ',' + y + ',' + z + ').\n' \
             + 'r2(' + y + ',1,1).\n' 
    return result
    
    
def consistent_answer_2(index):
    x = y = z = str(index)
    yy = 'a'+x
    n = 'm'+x
    result = 'r1(' + x + ',' + y + ',' + z + ').\n' \
             + 'r2(' + y + ',1,1).\n' \
             + 'r1(' + x + ',' + yy + ',' + z + ').\n' \
             + 'r2(' + yy + ',1,1).\n' \
             + 'r2(' + y + ',1,2).\n' \
             + 'r1(' + n + ',' + n + ',' + n + ').\n'
    return result
    
    
if __name__ == "__main__":
    argv = sys.argv[1:]
    assert len(argv) == 4    
    db = generate(2, [float(a) for a in argv], (inconsistent_answer, consistent_answer_1, consistent_answer_2, consistent_tuple, inconsistent_tuple))
    print(db)
    

