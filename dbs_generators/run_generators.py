import os

arities = [2,2,3,3,2,3,3]

inconsistency = 0.4
nb_taille_diff = 5
mult_taille = 1e3
rp_cons = 0.4
rp_inc = 0.2

for i in range(7):
    for j in range(1, nb_taille_diff):
        db_size = int(j * mult_taille)
        nb_consist = 1  # int(db_size / arities[i] * rp_cons)
        nb_inconsist = 0 # int(db_size / arities[i] * rp_inc)
        params = [db_size, inconsistency, nb_consist, nb_inconsist]
        # print('q'+str(i), params)
        
        cmd = 'python3 db' + str(i+1) + '.py ' + ' '.join(str(p) for p in params)
        db_file = '../generated_dbs/test/' + str(i+1) + "testing.txt"
        
        
        """
        + str(j)\
                  + '000_' + '_' + str(inconsistency) + '_'\
                  + "{:.2f}".format(nb_inconsist/(nb_consist+nb_inconsist)) + '.lp'
        """
        os.system(cmd + ' > ' + db_file)
        
