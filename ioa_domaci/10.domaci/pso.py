import random
import math

A = (1, 5, 1)
B = (3, 2, 0)
C = (5, 7, 1)
D = (6, 3, 3)


def distance(a, b):
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2 + (b[2] - a[2]) ** 2)


def opt_f(x):
    global A, B, C, D
    S1 = (x[0], x[1], x[2])
    S2 = (x[3], x[4], x[5])

    return distance(A, S1) + distance(B, S1) + distance(S1, S2) + distance(S2, C) + distance(S2, D)


agents = [[random.random()*6 for i in range(6)] for j in range(1000)]
v = [[0.1 for i in range(6)] for j in range(1000)]
per_best = [agents[i] for i in range(1000)]

general_best = agents[0]

for i in range(2000):

    for j in range(len(agents)):
        new_v = []
        for k in range(6):
            new_v.append(0.729 * v[j][k])

        for k in range(6):
            new_v[k] += 1.494 * random.random() * (per_best[j][k] - agents[j][k]) + 1.494 * random.random()*(general_best[k] - agents[j][k])

        for k in range(6):
            if new_v[k]>0.1:
                new_v[k]=0.1

        v[j]=new_v



    for j in range(len(agents)):
        for k in range(6):
            agents[j][k]+=v[j][k]
        my_val = opt_f(agents[j])
        if my_val < opt_f(per_best[j]):
            per_best[j] = agents[j]

        if my_val < opt_f(general_best):
            general_best = agents[j]



print("Konacne tacke su:")
print("S1 = ({0},{1},{2}) , S2 = ({3},{4},{5})".format(general_best[0],general_best[1],general_best[2],general_best[3],general_best[4],general_best[5]))
print("Minimalna duzina puta je:")
print(opt_f(general_best))
