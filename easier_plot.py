
f = open('results_test4.txt', 'r')
lines = f.readlines()
f.close()

abscisse = '0, 20, 40, 60, 80, 100\n'

fo = []
gt = []

for i in range(len(lines)):
    # j = i//5
    k = i%5
    line = lines[i]
    if k == 1:
        fo.append([float(measure) for measure in line.split(', ')[:-1]])
    elif k == 3:
        gt.append([float(measure) for measure in line.split(', ')[:-1]])

res = ""    

for i in range(len(fo[0])):
    res += abscisse
    res += ', '.join(["{:.2f}".format(ml[i]) for ml in fo]) + '\n'
    res += 'Q' + str(i+1) + ' - fo\n'
    res += abscisse 
    res += ', '.join(["{:.2f}".format(ml[i]) for ml in gt]) + '\n'
    res += 'Q' + str(i+1) + ' - gt\n'

print(res)
