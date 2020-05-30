import os

arities = [2,2,3,3,2,3,3]

db_size = 150000
nb_consist = 1
nb_inconsist = 0

inconsistenties = [0.2, 0.4, 0.6, 0.8]

# Consistent answer

for inconsistency in inconsistenties:
    for i in range(7):
        params = [db_size, inconsistency, nb_consist, nb_inconsist]
        # print('q'+str(i), params)

        cmd = 'python3 db' + str(i+1) + '.py ' + ' '.join(str(p) for p in params)
        db_file = '../generated_dbs/test2/con/' + str(i+1) + '_' + str(int(db_size/1000)) + 'k_' + str(inconsistency) + '.lp'
        os.system(cmd + ' > ' + db_file)

# Inconsistant
nb_consist = 1
nb_inconsist = 0

for inconsistency in inconsistenties:
    for i in range(7):
        params = [db_size, inconsistency, nb_consist, nb_inconsist]
        # print('q'+str(i), params)

        cmd = 'python3 db' + str(i+1) + '.py ' + ' '.join(str(p) for p in params)
        db_file = '../generated_dbs/test2/inc/' + str(i+1) + '_' + str(int(db_size/1000)) + 'k_' + str(inconsistency) + '.lp'
        os.system(cmd + ' > ' + db_file)

