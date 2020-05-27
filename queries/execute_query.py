import os


def write_lp_file(s: str): # Not used anymore
    rr_line = build_rr_line(parse_var_array(s))
    f = open(output_file, 'w')
    f.write(script)
    f.write(rr_line)
    f.close()
    
    
def build_rr_line(array: list): # Not used anymore
    res = ':- '
    for var in array:
        res += 'rr(_,_,' + var + ',_,_), '
    return res[:-2] + '.\n'
    
    
def parse_var_array(s: str, query='q'):
    q = query + '('
    return s.replace(q,'').replace(')','').strip('\n').split(' ')
   
    
def bash_cmd(cmd):
    stream = os.popen(cmd)
    return stream.readlines()
    
    
def write_file(filepath, msg):
    f = open(filepath, "w")
    f.write(msg)
    f.close()
    
    
def rm_file(filepath):
    os.system('rm ' + filepath)


def test_all_scripts(db_file, script, array, tmp_file):
    result = []
    time = 0.0
    for var in array:
        line = script(var)
        write_file(tmp_file, line)
        # print(line)
        cmd_result = bash_cmd('clingo ' + db_file + ' ' + tmp_file)
        time += float(cmd_result[-1].strip('\n').split(': ')[1][:-1])
        if cmd_result[3] == 'UNSATISFIABLE\n':
            result.append(var)  
    return time, str(len(result)) + ' consistent answers out of ' + str(len(array)) 
    
    
def execute_gt_query(db_file, script, query, tmp_file):
    write_file(tmp_file, query)
    output = bash_cmd('clingo ' + db_file + ' ' + tmp_file)
    rm_file(tmp_file)
    array = parse_var_array(output[4])
    # print(array)
    print(test_all_scripts(db_file, script, array, tmp_file))
    rm_file(tmp_file) 
    
    
def parse_argv(argv, script, query, tmp_file):
    if len(argv) != 2:
        print('Input file path expected as argument')
    else:
        execute_gt_query(argv[1], script, query, tmp_file)


def run_fo_query(db_file, fo_script):
    clingo_output = bash_cmd('clingo ' + db_file + ' ' + fo_script)
    array = parse_var_array(clingo_output[4], 'cqa')
    time = float(clingo_output[-1].strip('\n').split(': ')[1][:-1])
    print(time, len(array))

    
if __name__ == "__main__":
    import sys
    if len(sys.argv) != 4:
        print("3 arguments expected : number_query type_query path_to_db")
    else:
        n = sys.argv[1]
        query_type = sys.argv[2]
        db_file = sys.argv[3]
        assert os.path.isfile(db_file)
        assert query_type in ['fo','gt']
        if query_type == 'gt':
            module_name = 'gtq'+n
            module = __import__(module_name)
            execute_gt_query(db_file, module.get_script, module.query, module.tmp_file)
        else:
            fo_script = 'q' + n + 'fo.lp'
            run_fo_query(db_file, fo_script)
            
