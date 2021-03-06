import sys
import random
import argparse
import math

"""q1(z):=E x, y, v, w | r1(x | y, z) and r2(y | v, w)
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
    x2 = size
    for i in range(x1):
        res += "r1(x"+str(i)+",y"+str(i)+",z"+str(i)+")."
        res += "r2(y"+str(i)+",v"+str(i)+",w"+str(i)+").\n"
    for i in range(x1,x2):
        r1 = random.randint(0, x1-1)
        res += "r1(x"+str(i)+",y"+str(r1)+",z"+str(r1)+")."
        res += "r2(y"+str(r1)+",v"+str(r1)+",w"+str(r1)+").\n"
    return res


def generateNoInstance(size, inconsistency, error):
    res = ""
    i = 0

    noIncons = math.ceil(size*(1-inconsistency))

    for i in range(int(size/2)):
        if i<int(noIncons/2):
            res += "r1(x"+str(i)+",y"+str(i)+",z"+str(i)+")."
            res += "r2(y"+str(i)+",v"+str(i)+",w"+str(i)+").\n"
        else:
            r1 = random.randint(0, noIncons-1)
            res += "r1(x"+str(i)+",y"+str(r1)+",z"+str(r1)+")."
            res += "r2(y"+str(r1)+",v"+str(r1)+",w"+str(r1)+").\n"
        res += "r1(x"+str(i)+",y"+str(size+i)+",z"+str(size+i)+").\n"

    return res


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Database generator for the 3th query i.e. z|Ex,y,v,u,d:r1(x|y,z),r3(y|v),r2(v|u,d)")
    parser.add_argument('--instance', '-i', required=True, type=str,
                        nargs='+', help='the instance that may be return by the query')
    parser.add_argument('--size', '-s', required=True,
                        type=int, nargs='+', help='the size of the database')
    parser.add_argument('--inconsistency', '-c', required=True,
                        type=float, nargs='+', help='the ratio of tuples that violate the primary key')
    args = parser.parse_args()
    res = generateInstance(
        instance=args.instance[0], size=args.size[0], inconsistency=args.inconsistency[0])
    print(res)
