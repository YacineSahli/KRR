import sys

def generate(size, inconsistence, nb_consist_answers, nb_inconsistent_answers):
    
    nb_inconsistent_answers = int(nb_inconsistent_answers)
    nb_consist_answers = int(nb_consist_answers)
    nb_tuples = int(size/2)
    remaining_inconsistent_tuples = inconsistence * nb_tuples  # nb tuples to remove to have a consistent db
    answer = ""
    
    assert nb_inconsistent_answers <= remaining_inconsistent_tuples
    
    for i in range(nb_inconsistent_answers):
        answer += add_inconsistent_answer(i)
    
    remaining_inconsistent_tuples -= nb_inconsistent_answers  # For every inconsistent answer, a broken primary was added 
    
    start = nb_inconsistent_answers * 2  # All the numbers under this one are already used
    total_tuples = start  # Total tuples for one table
    for i in range(start, start + nb_consist_answers):
        if remaining_inconsistent_tuples > 0 and i % 2 == 0:
            answer += add_consistent_answer_2(i)
            remaining_inconsistent_tuples -= 1
            total_tuples += 2
        else:
            answer += add_consistent_answer_1(i)
        total_tuples += 1
    
    while remaining_inconsistent_tuples > 0:
        n = str(total_tuples)
        answer += 'r1(' + n + ',' + n + ',' + n + ').\n' + 'r2(w' + n + ',1,1).\n' \
                  + 'r1(' + n + ',p' + n + ',p' + n + ').\n' + 'r2(w' + n + ',2,1).\n'
        total_tuples += 2
        remaining_inconsistent_tuples -= 1
        
    while total_tuples < nb_tuples:
        n = str(total_tuples)
        answer += 'r1(' + n + ',' + n + ',' + n + ').\n' + 'r2(w' + n + ',1,1).\n' 
        total_tuples += 1
    
    print(answer)    
    
    
def add_inconsistent_answer(index):
    n = index * 2
    x = y = z = str(n)
    if index % 2 == 0:  # dangling
        yy = str(n+1)
        zz = z
    else:  # another_z
        zz = str(n+1)
        yy = y
    result = 'r1(' + x + ',' + y + ',' + z + ').\n' \
             + 'r2(' + y + ',1,1).\n' \
             + 'r1(' + x + ',' + yy + ',' + zz + ').\n' \
             + 'r2(' + y + ',1,2).\n'
    return result
    
    
def add_consistent_answer_1(index):
    x = y = z = str(index)
    result = 'r1(' + x + ',' + y + ',' + z + ').\n' \
             + 'r2(' + y + ',1,1).\n' 
    return result
    
    
def add_consistent_answer_2(index):
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
    generate(*[float(a) for a in argv])

