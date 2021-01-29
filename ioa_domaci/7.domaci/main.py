import math
import random
import numpy as np
import scipy.special as sp
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
start_temp = 32*1024*1024*1.0

s = [173669, 275487, 1197613, 1549805, 502334, 217684, 1796841, 274708,
631252, 148665, 150254, 4784408, 344759, 440109, 4198037, 329673, 28602,
144173, 1461469, 187895, 369313, 959307, 1482335, 2772513, 1313997, 254845,
486167, 2667146, 264004, 297223, 94694, 1757457, 576203, 8577828, 498382,
8478177, 123575, 4062389, 3001419, 196884, 617991, 421056, 3017627, 131936,
1152730, 2676649, 656678, 4519834, 201919, 56080, 2142553, 326263, 8172117,
2304253, 4761871, 205387, 6148422, 414559, 2893305, 2158562, 465972, 304078,
1841018, 1915571]

memory = int(math.pow(2,26))
absolute_minimum=33
abs_min_x=0
random.seed()

def new_x(h,x):

    i = 0
    changes=[]
    num_changes=random.randint(1,h)
    while i < num_changes:
        num = random.randint(0,63)
        found = False
        for j in range(len(changes)):
            if num == changes[j]:
                found = True
                break

        if found==True:
            continue
        else:
            changes.append(num)
            i = i+1

    nx = x
    for k in range(len(changes)):
        l = changes[k]
        state = (nx >> l) & 1
        mask = 0
        if state==1:
            mask = ~(1 << l)
            nx = nx &mask
        else:
            mask = (1 << l)
            nx = nx | mask

    return nx

def f(x):
    f_num = memory
    ret_x = x
    i=0
    while ret_x>0:
        if(ret_x & 1==1):
            f_num = f_num-s[i]
        i = i+1
        ret_x=ret_x>>1

    if f_num<0:
        return memory

    return f_num




def kaljenje():
    global absolute_minimum
    global abs_min_x
    t = start_temp
    x = random.randint(0,int(math.pow(2,64)-1))
    num_iter = 100000
    h = 0
    min_row=[]
    old_min=-1
    for i in range(1,num_iter+1):
        if(old_min==-1 or old_min>f(x)):
            old_min=f(x)
        min_row.append(old_min)
        if(old_min<absolute_minimum):
            absolute_minimum = old_min
            abs_min_x = x

        if(i==1):
            h = 64
        elif i==num_iter:
            h = 1
        else:
            h = int(((1-64)*(i-1)*1.0/(num_iter-1))+64)

        t = 0.95*t
        nx = new_x(h,x)
        diff = f(nx)-f(x)
        if diff<0:
            x = nx
        else:
            prob = math.exp(-diff*1.0/t)
            list = [0,1]
            r = np.random.choice(list,1,p=[1-prob,prob])
            if r[0]==1:
                x = nx
    return min_row


collective_minimum=[]

for i in range(20):
    collective_minimum.append(kaljenje())

print("Najmanja moguca vrednost je:")
print(absolute_minimum)
print("Najmanje moguce resenje je:")
print("{0:b}".format(abs_min_x))

x_ax = np.linspace(1,100000,100000)
fig = plt.figure()
fig.subplots_adjust(hspace=1)
ax1 = fig.add_subplot(211)
for i in range(20):
    ax1.loglog(x_ax,collective_minimum[i],label="i = "+str(i))
ax1.grid(True)
ax1.title.set_text("Kumulativni minimumi")
ax1.set_xlabel("iteracije")
ax1.set_ylabel("optimizacije")
ax1.legend(loc="upper right")


best_med_sol=[]
for i in range(100000):
    sum_el=0
    for j in range(20):
        sum_el+=collective_minimum[j][i]

    sum_el = sum_el/20
    best_med_sol.append(sum_el)

ax2 = fig.add_subplot(212)
ax2.loglog(x_ax,best_med_sol)
ax2.grid(True)
ax2.title.set_text("Najbolje srednje resenje")
ax2.set_xlabel("iteracije")
ax2.set_ylabel("optimizacije")


plt.show()

























