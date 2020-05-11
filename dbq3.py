import sys
import random
import argparse
import math

"""q3(z):=E x, y, v, u, d | r1(x | y, z) et r3(y | v) et r2(v | u, d)
"""


def generateInstance(instance="yes", size=3, inconsistency=0, error=0):
    if instance == "yes":
        return generateYesInstance(size, inconsistency)
    elif instance == "no":
        return generateNoInstance(size, inconsistency, error)


def generateYesInstance(size, inconsistency):
    res = ""
    """ for i in range(size):
        res += "r1(x"+str(i)+",y"+str(i)+",z)."
        res += "r2(v"+str(i)+",u"+str(i)+",d"+str(i)+")."
        res += "r3(y"+str(i)+",v"+str(i)+").\n"
        r=random.random()
        if r<inconsistency:
            res += "r1(x"+str(i)+",y"+str(size+i)+",z)."
            res += "r2(v"+str(i)+",u"+str(size+i)+",d"+str(size+i)+")."
            res += "r3(y"+str(i)+",v"+str(size+i)+").\n"
    return res """

    i = 0
    x1 = math.ceil(size*(1-inconsistency))
    x2 = math.floor(size*inconsistency)
    for i in range(x1):
        res += "r1(x"+str(i)+",y"+str(i)+",z)."
        res += "r2(v"+str(i)+",u"+str(i)+",d"+str(i)+")."
        res += "r3(y"+str(i)+",v"+str(i)+").\n"
    for i in range(x2):
        r1 = random.randint(0, x1-1)
        r2 = random.randint(0, x1-1)
        r3 = random.randint(0, x1-1)
        res += "r1(x"+str(r1)+",y"+str(r3)+",z)."
        res += "r2(v"+str(r2)+",u"+str(x1+i)+",d"+str(x1+i)+")."
        res += "r3(y"+str(r3)+",v"+str(r2)+").\n"
    return res


def generateNoInstance(size, inconsistency, error):
    res = ""
    i = 0
    x1 = math.ceil(size*(1-inconsistency))
    x2 = math.floor(size*inconsistency)
    x31 = math.ceil(x1*(1-error))
    x32 = math.floor(x2*(1-error))
    for i in range(x1):
        res += "r1(x"+str(i)+",y"+str(i)+",z)."
        res += "r2(v"+str(i)+",u"+str(i)+",d"+str(i)+")."
        res += "r3(y"+str(i)+",v"+str(i)+").\n"
        if i > x31:
            re = random.random()
	# zz
            res += "r1(x"+str(i)+",y"+str(i)+",z"+str(i+size)+").\n"
    for i in range(x2-1):
        r1 = random.randint(0, x1-1)
        r2 = random.randint(0, x1-1)
        r3 = random.randint(0, x1-1)
        if i < x32:
            res += "r1(x"+str(r1)+",y"+str(r3)+",z)."
            res += "r2(v"+str(r2)+",u"+str(x1+i)+",d"+str(x1+i)+")."
            res += "r3(y"+str(r3)+",v"+str(r2)+").\n"
        else:
            res += "r1(x"+str(r1)+",y"+str(r3+size)+",z)."
            res += "r2(v"+str(r2)+",u"+str(x1+i)+",d"+str(x1+i)+")."
            res += "r3(y"+str(r3)+",v"+str(r2+size)+").\n"
    return res


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Database generator for the 3rd query i.e. z|Ex,y,v,u,d:r1(x|y,z),r3(y|v),r2(v|u,d)")
    parser.add_argument('--instance', '-i', required=True, type=str,
                        nargs='+', help='the instance that may be return by the query')
    parser.add_argument('--size', '-s', required=True,
                        type=int, nargs='+', help='the size of the database')
    parser.add_argument('--inconsistency', '-c', required=True,
                        type=float, nargs='+', help='the ratio of tuples that violate the primary key')
    parser.add_argument('--error', '-e', required=True,
                        type=float, nargs='+', help='the ratio of tuples that violate the query')
    args = parser.parse_args()
    res = generateInstance(
        instance=args.instance[0], size=args.size[0], inconsistency=args.inconsistency[0], error=args.error[0])
    print(res)
