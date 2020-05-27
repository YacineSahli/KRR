import os

arities = [2,2,3,3,2,3,3]

inconsistency = 0.4

for i in range(7):
    for j in range(1,3):
        db_size = int(j * 1e3)
        nb_consist = int(db_size / arities[i] * 0.4)
        nb_inconsist = int(db_size / arities[i] * 0.2)
        params = [db_size, inconsistency, nb_consist, nb_inconsist]
        
        cmd = 'python3 db' + str(i+1) + '.py ' + ' '.join(str(p) for p in params)
        db_file = '../generated_dbs/q' + str(i+1) + '_' + str(j)\
                  + '000_' + '_' + str(inconsistency) + '_'\
                  + "{:.2f}".format(nb_inconsist/(nb_consist+nb_inconsist)) + '.lp'
        os.system(cmd + ' > ' + db_file)
        
