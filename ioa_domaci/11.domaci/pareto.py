import math
import random
import numpy as np
import scipy.special as sp
import matplotlib

matplotlib.use('TkAgg')
import matplotlib.pyplot as plt


def f1(x1, x2):
    return 2 * math.pow(x1, 2) + math.pow(x2, 2)


def f2(x1, x2):
    return -1 * math.pow(x1 - x2, 2)


dots_one = []
pareto_dots_one = []
dots_two = []
pareto_dots_two = []

random.seed()


def func1():
    global dots_one, pareto_dots_one
    for i in range(10000):
        one = random.random() * 2 - 1
        two = random.random() * 2 - 1
        dots_one.append((one, two))

    for i in range(10000):
        dominated = False
        for j in range(10000):
            if not (i == j):
                sol_i = (f1(dots_one[i][0], dots_one[i][1]), f2(dots_one[i][0], dots_one[i][1]))
                sol_j = (f1(dots_one[j][0], dots_one[j][1]), f2(dots_one[j][0], dots_one[j][1]))

                if (sol_j[0] < sol_i[0] and sol_j[1] <= sol_i[1]) or (sol_j[1] < sol_i[1] and sol_j[0] <= sol_i[0]):
                    dominated = True
                    break

        if not dominated:
            pareto_dots_one.append(dots_one[i])


def func2():
    global dots_two, pareto_dots_two
    count = 0
    while count < 10000:
        one = random.random() * 2 - 1
        two = random.random() * 2 - 1
        if one * two + 0.25 >= 0:
            dots_two.append((one, two))
            count += 1

    for i in range(10000):
        dominated = False
        for j in range(10000):
            if not (i == j):
                sol_i = (f1(dots_two[i][0], dots_two[i][1]), f2(dots_two[i][0], dots_two[i][1]))
                sol_j = (f1(dots_two[j][0], dots_two[j][1]), f2(dots_two[j][0], dots_two[j][1]))

                if (sol_j[0] < sol_i[0] and sol_j[1] <= sol_i[1]) or (sol_j[1] < sol_i[1] and sol_j[0] <= sol_i[0]):
                    dominated = True
                    break

        if not dominated:
            pareto_dots_two.append(dots_two[i])


func1();
func2();


x_one=[]
y_one=[]
pareto_x_one=[]
pareto_y_one=[]
x_two=[]
y_two=[]
pareto_x_two=[]
pareto_y_two=[]
for i in range(10000):
    x_one.append(dots_one[i][0])
    y_one.append(dots_one[i][1])
    x_two.append(dots_two[i][0])
    y_two.append(dots_two[i][1])

for i in range(len(pareto_dots_one)):
    pareto_x_one.append(pareto_dots_one[i][0])
    pareto_y_one.append(pareto_dots_one[i][1])

for i in range(len(pareto_dots_two)):
    pareto_x_two.append(pareto_dots_two[i][0])
    pareto_y_two.append(pareto_dots_two[i][1])




plt.scatter(x_one, y_one, label='Regular dots',s=2)
plt.scatter(pareto_x_one, pareto_y_one, label='Pareto front',s=2)

plt.grid(True)
plt.title("Problem 1(bez dodatnog uslova,tacke iz domena)")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.show()

plt.scatter(x_two, y_two, label='Regular dots',s=2)
plt.scatter(pareto_x_two, pareto_y_two, label='Pareto front',s=2)

plt.grid(True)
plt.title("Problem 2(sa dodatnim uslovom,tacke iz domena)")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.show()

general_f_one_one=[]
general_f_one_two=[]
pareto_f_one_one=[]
pareto_f_one_two=[]
general_f_two_one=[]
general_f_two_two=[]
pareto_f_two_one=[]
pareto_f_two_two=[]

for i in range(10000):
    general_f_one_one.append(f1(dots_one[i][0],dots_one[i][1]))
    general_f_one_two.append(f2(dots_one[i][0],dots_one[i][1]))
    general_f_two_one.append(f1(dots_two[i][0],dots_two[i][1]))
    general_f_two_two.append(f2(dots_two[i][0],dots_two[i][1]))

for i in range(len(pareto_dots_one)):
    pareto_f_one_one.append(f1(pareto_dots_one[i][0],pareto_dots_one[i][1]))
    pareto_f_one_two.append(f2(pareto_dots_one[i][0],pareto_dots_one[i][1]))

for i in range(len(pareto_dots_two)):
    pareto_f_two_one.append(f1(pareto_dots_two[i][0], pareto_dots_two[i][1]))
    pareto_f_two_two.append(f2(pareto_dots_two[i][0], pareto_dots_two[i][1]))



plt.scatter(general_f_one_one, general_f_one_two, label='Function dots',s=2)
plt.scatter(pareto_f_one_one, pareto_f_one_two, label='Pareto front',s=2)

plt.grid(True)
plt.title("Problem 1(bez dodatnog uslova,f1-f2 tacke)")
plt.xlabel("f1")
plt.ylabel("f2")
plt.legend()
plt.show()

plt.scatter(general_f_two_one, general_f_two_two, label='Function dots',s=2)
plt.scatter(pareto_f_two_one, pareto_f_two_two, label='Pareto front',s=2)

plt.grid(True)
plt.title("Problem 2(sa dodatnim uslovom,f1-f2 tacke)")
plt.xlabel("f1")
plt.ylabel("f2")
plt.legend()
plt.show()



