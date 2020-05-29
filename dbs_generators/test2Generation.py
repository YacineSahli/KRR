import os

arities = [2,2,3,3,2,3,3]

nbr_taille_diff = 1
mult_taille = 1e5
nb_consist = 1
nb_inconsist = 0

# Consistent answer

inconsistency = 0.2

for i in range(7):
    db_size = int(1 * mult_taille)
    params = [db_size, inconsistency, nb_consist, nb_inconsist]
    # print('q'+str(i), params)

    cmd = 'python3 db' + str(i+1) + '.py ' + ' '.join(str(p) for p in params)
    db_file = '../generated_dbs/test2/con/' + str(i+1) + '_' + str(db_size)\
               + '_' + str(inconsistency) + '_'\
              + "{:.2f}".format(nb_inconsist/(nb_consist+nb_inconsist)) + '.lp'
    os.system(cmd + ' > ' + db_file)


inconsistency = 0.4
for i in range(7):
    db_size = int(1 * mult_taille)
    params = [db_size, inconsistency, nb_consist, nb_inconsist]
    # print('q'+str(i), params)

    cmd = 'python3 db' + str(i+1) + '.py ' + ' '.join(str(p) for p in params)
    db_file = '../generated_dbs/test2/con/' + str(i+1) + '_' + str(db_size)\
               + '_' + str(inconsistency) + '_'\
              + "{:.2f}".format(nb_inconsist/(nb_consist+nb_inconsist)) + '.lp'
    os.system(cmd + ' > ' + db_file)




inconsistency = 0.6
for i in range(7):
    db_size = int(1 * mult_taille)
    params = [db_size, inconsistency, nb_consist, nb_inconsist]
    # print('q'+str(i), params)

    cmd = 'python3 db' + str(i+1) + '.py ' + ' '.join(str(p) for p in params)
    db_file = '../generated_dbs/test2/con/' + str(i+1) + '_' + str(db_size)\
               + '_' + str(inconsistency) + '_'\
              + "{:.2f}".format(nb_inconsist/(nb_consist+nb_inconsist)) + '.lp'
    os.system(cmd + ' > ' + db_file)



inconsistency = 0.8
for i in range(7):
    db_size = int(1 * mult_taille)
    params = [db_size, inconsistency, nb_consist, nb_inconsist]
    # print('q'+str(i), params)

    cmd = 'python3 db' + str(i+1) + '.py ' + ' '.join(str(p) for p in params)
    db_file = '../generated_dbs/test2/con/' + str(i+1) + '_' + str(db_size)\
               + '_' + str(inconsistency) + '_'\
              + "{:.2f}".format(nb_inconsist/(nb_consist+nb_inconsist)) + '.lp'
    os.system(cmd + ' > ' + db_file)

# Inconsistant
nb_consist = 1
nb_inconsist = 0
inconsistency=0.2

for i in range(7):
    db_size = int(1 * mult_taille)
    params = [db_size, inconsistency, nb_consist, nb_inconsist]
    # print('q'+str(i), params)

    cmd = 'python3 db' + str(i+1) + '.py ' + ' '.join(str(p) for p in params)
    db_file = '../generated_dbs/test2/inc/' + str(i+1) + '_' + str(db_size)\
               + '_' + str(inconsistency) + '_'\
              + "{:.2f}".format(nb_inconsist/(nb_consist+nb_inconsist)) + '.lp'
    os.system(cmd + ' > ' + db_file)


inconsistency = 0.4
for i in range(7):
    db_size = int(1 * mult_taille)
    params = [db_size, inconsistency, nb_consist, nb_inconsist]
    # print('q'+str(i), params)

    cmd = 'python3 db' + str(i+1) + '.py ' + ' '.join(str(p) for p in params)
    db_file = '../generated_dbs/test2/inc/' + str(i+1) + '_' + str(db_size)\
               + '_' + str(inconsistency) + '_'\
              + "{:.2f}".format(nb_inconsist/(nb_consist+nb_inconsist)) + '.lp'
    os.system(cmd + ' > ' + db_file)




inconsistency = 0.6
for i in range(7):
    db_size = int(1 * mult_taille)
    params = [db_size, inconsistency, nb_consist, nb_inconsist]
    # print('q'+str(i), params)

    cmd = 'python3 db' + str(i+1) + '.py ' + ' '.join(str(p) for p in params)
    db_file = '../generated_dbs/test2/inc/' + str(i+1) + '_' + str(db_size)\
               + '_' + str(inconsistency) + '_'\
              + "{:.2f}".format(nb_inconsist/(nb_consist+nb_inconsist)) + '.lp'
    os.system(cmd + ' > ' + db_file)



inconsistency = 0.8
for i in range(7):
    db_size = int(1 * mult_taille)
    params = [db_size, inconsistency, nb_consist, nb_inconsist]
    # print('q'+str(i), params)

    cmd = 'python3 db' + str(i+1) + '.py ' + ' '.join(str(p) for p in params)
    db_file = '../generated_dbs/test2/inc/' + str(i+1) + '_' + str(db_size)\
               + '_' + str(inconsistency) + '_'\
              + "{:.2f}".format(nb_inconsist/(nb_consist+nb_inconsist)) + '.lp'
    os.system(cmd + ' > ' + db_file)
