import sys
import random
import argparse

def generate_db(relations_arity, relations_size, pk_size, inconsistency):
    """
    Generates a database in ASP.
    :param relations_arity: a tuple (a_1, ..., a_n) where a_i is the arity of the i-th relation
    :param relations_size: a tuple (s_1, ..., s_n) where s_i is the number of tuples of the i-th relation
    :param pk_size: a tuple (pk_1, ..., pk_n) where pk_i the number of elements in the primary key of the i-th relation (so 1 <= pk_i <= a_i)
    :param inconsistency: a tuple (i_1, ..., i_n) where i_i is the ratio of tuples that violate the primary key for the i_th relation
    :return: A string that corresponds to the database in ASP.
    """
    result = ""
    for i in range(len(relations_arity)):
        start = "r" + str(i+1) + "("
        size = 0
        cnt_array = [1]*relations_arity[i]
        while size < relations_size[i]:
            result += start
            for cnt in cnt_array[:-1]:
                result += str(cnt) + ","
            result += str(cnt_array[-1])
            p = random.random()
            if p < inconsistency[i]:
                update_array(cnt_array, pk_size[i], len(cnt_array)-1)
            else:
                update_array(cnt_array, 0, pk_size[i]-1)
                for index in range(pk_size[i], len(cnt_array)):
                    cnt_array[index] = 1
            result += ").\n"
            size += 1
    return result

def update_array(array, start, stop):
    """
    Increments one element in the array between the specified bounds
    :param array: the list that will be modified
    :param start: the lower bound
    :param stop: the upper bound
    :return: None
    """
    index = stop
    while index > start and array[index] > array[index-1]:
        index -= 1
    array[index] += 1

def verify_input(relations_arity,relations_size,pkSize,inconsistency):
    if not len(relations_arity) == len(relations_size) == len(pkSize) == len(inconsistency):
        sys.exit("INPUT ERRR: The length of the relations_arity, relations_size, pkSize and inconsistency should all be equal !")

if __name__ == "__main__":
    random.seed(a=42)
    parser = argparse.ArgumentParser(description='Database generator for ASP(Answer Set Programming).')
    parser.add_argument('--relations_arity', '-a', required=True , type=int, nargs='+',
                        help='a tuple a_1 a_2 ... a_n) where a_i is the arity of the i-th relation')
    parser.add_argument('--relations_size', '-r', required=True, type=int, nargs='+',
                        help='a tuple s_1 s_2 ... s_n where s_i is the number of tuples of the i-th relation')
    parser.add_argument('--pkSize','-p',required=True , type=int, nargs='+',
                        help='a tuple pk_1 pk_2 ... pk_n where pk_i the number of elements in the primary key of the i-th relation (so 1 <= pk_i <= a_i)')
    parser.add_argument('--inconsistency','-i', required=True , type=float, nargs='+',
                        help='a tuple i_1 i_2 ... i_n where i_i is the ratio of tuples that violate the primary key for the i_th relation')
    args = parser.parse_args()
    verify_input(args.relations_arity,args.relations_size,args.pkSize,args.inconsistency)
    result = generate_db(args.relations_arity,args.relations_size,args.pkSize,args.inconsistency)
    print(result)
    
