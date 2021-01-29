import math
import random
import numpy as np
import scipy.special as sp
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

s = [173669, 275487, 1197613, 1549805, 502334, 217684, 1796841, 274708,
     631252, 148665, 150254, 4784408, 344759, 440109, 4198037, 329673, 28602,
     144173, 1461469, 187895, 369313, 959307, 1482335, 2772513, 1313997, 254845,
     486167, 2667146, 264004, 297223, 94694, 1757457, 576203, 8577828, 498382,
     8478177, 123575, 4062389, 3001419, 196884, 617991, 421056, 3017627, 131936,
     1152730, 2676649, 656678, 4519834, 201919, 56080, 2142553, 326263, 8172117,
     2304253, 4761871, 205387, 6148422, 414559, 2893305, 2158562, 465972, 304078,
     1841018, 1915571]

memory = int(math.pow(2, 26))
absolute_minimum = memory
abs_min_x = 0
random.seed()


def f(x):
    f_num = memory
    ret_x = x
    i = 0
    while ret_x > 0:
        if ret_x & 1 == 1:
            f_num = f_num - s[i]
        i = i + 1
        ret_x = ret_x >> 1

    if f_num < 0:
        return memory

    return f_num




def darwin():
    global absolute_minimum
    global abs_min_x
    min_row = []
    old_min = -1
    generation = []
    for i in range(2000):
        generation.append(random.randint(1000, int(math.pow(2, 64) - 1)))

    for i in range(50):
        for j in range(2000):
            x = f(generation[j])
            if old_min == -1 or old_min > x:
                old_min = x

            if absolute_minimum > x:
                absolute_minimum = x
                abs_min_x = generation[j]

        min_row.append(old_min)
        best_members = []

        generation.sort(key=f)

        new_generation=[]

        for j in range(400):
            best_members.append(generation[j])


        while len(new_generation)<2000:
                p_select = [0, 1]
                ch = np.random.choice(p_select, 1, p=[0.4, 0.6])
                j = random.randint(0,399)
                k = random.randint(0,399)
                while j == k:
                    k = random.randint(0,399)

                if ch[0] == 1 and len(new_generation) < 2000:
                    nx = 0
                    ny = 0
                    a = random.randint(0, 63)
                    mask = 0xffffffffffffffff
                    mask = mask << a
                    nx = best_members[j] & mask
                    nx = nx | (best_members[k] & (~mask))
                    ny = best_members[k] & mask
                    ny = ny | (best_members[j] & (~mask))
                    new_generation.append(nx)
                    new_generation.append(ny)

        for j in range(2000):
            px_select = [0, 1]
            c = np.random.choice(px_select, 1, p=[0.92, 0.08])
            if c[0] == 1:
                b = random.randint(0, 63)
                mask = 1 << b
                if (new_generation[j] >> b) & 1:
                    new_generation[j] = new_generation[j] | mask
                else:
                    new_generation[j] = new_generation[j] & (~mask)

        generation = new_generation

    return min_row


collective_minimum = []

for i in range(20):
    collective_minimum.append(darwin())

print("Najmanja moguca vrednost je:")
print(absolute_minimum)
print("Najmanje moguce resenje je:")
print("{0:b}".format(abs_min_x))

x_ax = np.linspace(1, 50, 50)
fig = plt.figure()
fig.subplots_adjust(hspace=1)
ax1 = fig.add_subplot(211)
for i in range(20):
    ax1.loglog(x_ax, collective_minimum[i], label="i = " + str(i))
ax1.grid(True)
ax1.title.set_text("Kumulativni minimumi")
ax1.set_xlabel("generacije")
ax1.set_ylabel("optimizacije")
ax1.legend(loc="upper right")

best_med_sol = []
for i in range(50):
    sum_el = 0
    for j in range(20):
        sum_el += collective_minimum[j][i]

    sum_el = sum_el / 20
    best_med_sol.append(sum_el)

ax2 = fig.add_subplot(212)
ax2.loglog(x_ax, best_med_sol)
ax2.grid(True)
ax2.title.set_text("Najbolje srednje resenje")
ax2.set_xlabel("generacije")
ax2.set_ylabel("optimizacije")

plt.show()
