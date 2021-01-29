import scipy.optimize as opt
import numpy as np
import math




A=[
[480,650,580,390,0,0,0,0,0,0,0,0],
[0,0,0,0,480,650,580,390,0,0,0,0],
[0,0,0,0,0,0,0,0,480,650,580,390],
[1,1,1,1,0,0,0,0,0,0,0,0],
[0,0,0,0,1,1,1,1,0,0,0,0],
[0,0,0,0,0,0,0,0,1,1,1,1],
[1,0,0,0,1,0,0,0,1,0,0,0],
[0,1,0,0,0,1,0,0,0,1,0,0],
[0,0,1,0,0,0,1,0,0,0,1,0],
[0,0,0,1,0,0,0,1,0,0,0,1]
]

B=[6800,8700,4300,10,16,8,18,15,23,12]

C=[-310,-380,-350,-285,-310,-380,-350,-285,-310,-380,-350,-285]

def f(x):
    return (310*(x[0]+x[4]+x[8])+380*(x[1]+x[5]+x[9])+350*(x[2]+x[6]+x[10])+285*(x[3]+x[7]+x[11]))

res = opt.linprog(C,A,B)

x = res.x


m_el = f(x)

for i in range(12):
    x[i]=math.floor(x[i])

m_el = f(x)
for i in range(12):
    el = x[i]
    poss_el = el-3
    for j in range(6):
        x[i] = poss_el
        poss_b = np.matmul(A, x)
        diff = np.subtract(B, poss_b)
        found = False
        for k in range(10):
            if diff[k] < 0:
                found = True
                break

        if found:
            x[i] = el
            continue

        if f(x) > m_el:
            m_el = f(x)
            el = x[i]
        else:
            x[i] = el
        poss_el = poss_el + 1


for i in range(12):
    print("%d"%x[i])

print
print "Rezultat funkcije je:"

m_el = f(x)
print ("%d"%m_el)






