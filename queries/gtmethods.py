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
    
    
def parse_var_array(s: str):
    return s.replace('q(','').replace(')','').strip('\n').split(' ')
   
    
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
        result.append(cmd_result[3])
        time += float(cmd_result[-1].strip('\n').split(': ')[1][:-1])
        if cmd_result[3] == 'UNSATISFIABLE\n':
            result.append(True)
        else:
            result.append(False)
            return "UNSAT", time  # To stop the program once a counter-example is found
    # if result.count(True) != len(result):   #  If you want not stop the program before
    #    return "UNSAT", time
    return "SAT", time
    
    
def parse_argv(argv, script, query, output_file, tmp_file):
   if len(argv) != 2:
        print('Input file path expected as argument')
   else:
        db_file = argv[1]
        write_file(tmp_file, query)
        output = bash_cmd('clingo ' + db_file + ' ' + tmp_file)
        rm_file(tmp_file)
        array = parse_var_array(output[4])
        # print(array)
        print(test_all_scripts(db_file, script, array, tmp_file))
        

