import random

# Pour générer un yes-instance de q1, on veut :
# - imposer que le 3e élément de r1 soit toujours le même
# - A chaque fois qu'un y (2e position dans r1) différent est ajouté, on ajoute une ligne commençant par y dans r2
def generate_yes_instance_q1(relations_size, inconsistency_deg, block_size):
    """
    Generates a yes-instance for q1
    :param relations_size: The number of tuples in r1
    :param inconsistency_deg: A float between 0 and 1, the proportion a violated primary keys
    :param block_size: An int, for each violated key, the number of tuples that violates this key
    :return: A string that corresponds to the database in ASP.
    """
    r1 = ""
    r2 = ""
    
    # r_size = nb_blocks * deg * block_size + (1 - deg) * nb_blocks
    nb_blocks = int(relations_size / ((inconsistency_deg * block_size) + (1- inconsistency_deg)))
    z = 1  # The value of z must be always the same
    v = 1  # As we don't care about v and w, we give always the same value (maybe a random value or something other is better)
    w = 1   
    for i in range(nb_blocks):
        r1 += 'r1(' + str(i+1) + ',' + str(i+1) + ',' + str(z) + ').\n'
        r2 += 'r2(' + str(i+1) + ',' + str(v) + ',' + str(w) + ').\n'
    # Now we add the inconsistency
    bound = int(inconsistency_deg * nb_blocks)
    for i in range(0, nb_blocks, bound):
        index = random.randrange(i, min(i+bound, nb_blocks))
        for j in range(block_size):
            y = random.randrange(nb_blocks+1, nb_blocks*2)
            r1 += 'r1(' + str(index) + ',' + str(y) + ',' + str(z) + ').\n'
            r2 += 'r2(' + str(y) + ',' + str(v) + ',' + str(w) + ').\n'
    return r1 + r2
        
        
if __name__ == "__main__":
    import sys
    if len(sys.argv) != 4:
        print("Wrong number of arguments : 4 expected")
    print(generate_yes_instance_q1(int(sys.argv[1]), float(sys.argv[2]), int(sys.argv[3])))
    
