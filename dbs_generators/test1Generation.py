import os

arities = [2,2,3,3,2,3,3]

def generatedb(inconsistency,mult_taille,nbr_taille_diff,nb_con,nb_inc,path):
    for i in range(7):
        for j in range(1,nbr_taille_diff+1):
            db_size = int(j * mult_taille)
            nb_consist = nb_con
            nb_inconsist = nb_inc
            params = [db_size, inconsistency, nb_consist, nb_inconsist]
            # print('q'+str(i), params)

            cmd = 'python3 db' + str(i+1) + '.py ' + ' '.join(str(p) for p in params)
            db_file = '../generated_dbs/test1/' + path+"/" + str(i+1) + '_' + str(db_size) + '_' + str(inconsistency) + '_'+ str(nb_consist)+"_"+str(nb_inconsist) + '.lp'
            os.system(cmd + ' > ' + db_file)

if __name__ == "__main__":
    inconsistency = 0.4
    nbr_taille_diff=5
    mult_taille=2500
    nb_con=1
    nb_inc=0
    generatedb(inconsistency,mult_taille,nbr_taille_diff,1,0,"con")
    generatedb(inconsistency,mult_taille,nbr_taille_diff,0,1,"inc")
