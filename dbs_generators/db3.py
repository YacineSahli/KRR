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
        total_tuples += 3
        remaining_inconsistent_tuples -= 1  # For every inconsistent answer, a broken primary key was added 
        answer += inconsistent_answer(n, yy, zz)
        
    
    start = total_tuples  # Total tuples for one table
    for i in range(start, start + nb_consist_answers):
        if remaining_inconsistent_tuples > 0 and i % 2 == 0:
            answer += consistent_answer_2(i)
            remaining_inconsistent_tuples -= 1
            total_tuples += 2
        else:
            answer += consistent_answer_1(i)
        total_tuples += 1
    
    while remaining_inconsistent_tuples > 0:
        n = str(total_tuples)
        size = min(4, remaining_inconsistent_tuples)
        if remaining_inconsistent_tuples >= nb_tuples - total_tuples:
            size = remaining_inconsistent_tuples
        answer += inconsistent_tuple(n, size)
        total_tuples += 1 + size
        remaining_inconsistent_tuples -= size
        
    while total_tuples < nb_tuples:
        n = str(total_tuples)
        answer += consistent_tuple(n)
        total_tuples += 1
    
    return answer    

        
def consistent_tuple(n):
    return 'r1(' + n + ',' + n + ',' + n + ').\n' + 'r2(w' + n + ',1,1).\n' + 'r3(q' + n + ',q' + n + ').\n'
 
    
def inconsistent_tuple(n, size):
    result = 'r1(' + n + ',' + n + ',' + n + ').\n' + 'r2(w' + n + ',1,1).\n' + 'r3(' + n + ',' + n + ').\n'
    for i in range(size):
        result += 'r1(' + n + ',p' + str(i+2) + ',p' + n + ').\n' + 'r2(w' + n + ',1,2).\n' + 'r3(' + n + ',m' + str(i+2) + ').\n'
    return result

    
    
def inconsistent_answer(n, yy, zz):
    x = y = z = v = n
    o = 'o' + x
    k = 'k' + x
    m = 'm' + x
    result = 'r1(' + x + ',' + y + ',' + z + ').\n' \
             + 'r3(' + y + ',' + v + ').\n'\
             + 'r2(' + v + ',1,1).\n' \
             + 'r1(' + x + ',' + yy + ',' + zz + ').\n' \
             + 'r3(' + y + ',o' + k + ').\n'\
             + 'r2(' + k + ',1,1).\n' \
             + 'r1(' + o + ',' + o + ',' + o + ').\n' \
             + 'r3(' + m + ',o' + m + ').\n' \
             + 'r2(' + k + ',2,1).\n'
    return result
    
    
def consistent_answer_1(index):
    x = y = z = v = str(index)
    result = 'r1(' + x + ',' + y + ',' + z + ').\n' \
             + 'r3(' + y + ',' + v + ').\n'\
             + 'r2(' + v + ',1,1).\n' 
    return result
    
    
def consistent_answer_2(index):
    x = y = z = v = str(index)
    yy = 'a'+x
    o = 'o'+x
    result = 'r1(' + x + ',' + y + ',' + z + ').\n' \
             + 'r3(' + y + ',' + v + ').\n'\
             + 'r2(' + v + ',1,1).\n' \
             + 'r1(' + x + ',' + yy + ',' + z + ').\n' \
             + 'r3(' + yy + ',' + v + ').\n'\
             + 'r2(' + o + ',1,1).\n' \
             + 'r1(' + o + ',' + o + ',' + o + ').\n' \
             + 'r3(' + yy + ',' + o + ').\n'\
             + 'r2(' + o + ',1,2).\n' 
    return result
    
    
if __name__ == "__main__":
    argv = sys.argv[1:]
    assert len(argv) == 4    
    db = generate(3, [float(a) for a in argv], (inconsistent_answer, consistent_answer_1, consistent_answer_2, consistent_tuple, inconsistent_tuple))
    print(db)
    

