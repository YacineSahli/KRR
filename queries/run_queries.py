import sys
from execute_query import *

if __name__ == "__main__":

    q_values = [0,1,2,3,4,5,6]

    if len(sys.argv) != 4:
        print("3 arguments expected : input_file_rep input_file_model output_file")   
    else:
        db_rep = '../generated_dbs/' + sys.argv[1]
        db_model = sys.argv[2]
        output_file = sys.argv[3]
        result = ''
        
        result += 'FO : ' + db_rep + '/X' + db_model + '\n'
        for i in q_values:
            n = str(i+1)
            db_file = db_rep + '/' + n + db_model
            fo_script = 'q' + n + 'fo.lp'

            # result += str(run_fo_query(db_file, fo_script)[0]) + ', '
            print("DONE FO : ", i)
        
        result += '\n' 
        result += 'GT : ' + db_rep + '/X' + db_model + '\n'
        for i in q_values:
            n = str(i+1)
            db_file = db_rep + '/' + n + db_model
            module_name = 'gtq' + n
            module = __import__(module_name)
            result += str(execute_gt_query(db_file, module.get_script, module.query, module.tmp_file)[0]) + ', '
            print("DONE GT : ", i)
            
            
        result += '\n'
        result += '--------------------------------------- \n'    
        f = open(output_file, 'a')
        f.write(result)
        f.close()
        
