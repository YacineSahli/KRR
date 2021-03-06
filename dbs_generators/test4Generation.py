import os

arities = [2,2,3,3,2,3,3]

def generatedb(inconsistency,nr):
    for i in range(7):
        for rp_inc in range(0,nr+1,20):
            db_size = 3000
            nb_consist = nr-rp_inc
            nb_inconsist = rp_inc
            params = [db_size, inconsistency, nb_consist, nb_inconsist]
            
            cmd = 'python3 db' + str(i+1) + '.py ' + ' '.join(str(p) for p in params)
            db_file = '../generated_dbs/test4/' + str(i+1) + '_' + str(db_size) + '_' + str(inconsistency) + '_'+ str(nb_consist)+"_"+str(nb_inconsist) + '.lp'
            os.system(cmd + ' > ' + db_file)
        
if __name__ == "__main__":
    inconsistency = 0.4
    nr=100
    generatedb(inconsistency,nr)
