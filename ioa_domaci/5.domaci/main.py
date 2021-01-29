import scipy.optimize
import math
import random
import numpy as np
import scipy.special as sp
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt


def yout(w,x):
    num = 0.0
    for i in range(5):
        num = num+w[i+5]*math.tanh(w[i]*x)

    num = math.tanh(num)

    return num

def ytraining(x):
    return 0.5*math.sin(math.pi*x)

def opt_f(w):
    for i in range(10):
        if w[i]<-10 or w[i]>10 :
            w[i]=random.random()*20-10

    x=-1.0
    num=0.0
    while x <= 1.0:
        num = num + math.pow(yout(w, x)-ytraining(x), 2)
        x = x+0.1
    num = math.sqrt(num)
    return num

w = []
random.seed()
while len(w) < 10:
    number = random.random()*20 -10
    w.append(number)

solution_fun = 1.0
while solution_fun>=1e-2:
    sol = scipy.optimize.minimize(opt_f,w,args=(),method='nelder-mead')
    w = sol.x
    solution_fun=opt_f(w)

print("Koeficijenti za cvorove:")
for i in range(10):
    print("%.15f" % w[i])
print
print("Minimalna vrednost optimizacione f-je:")
print("%.15f" % solution_fun)

x = np.linspace(-1, 1, 1000)
yout_arr=[]
ytraining_arr=[]
for i in range(len(x)):
    yout_arr.append(yout(w, x[i]))
    ytraining_arr.append(ytraining(x[i]))


plt.plot(x, yout_arr, label='YOut(x)')
plt.plot(x, ytraining_arr, label='YTraining(x)')

plt.xlim((-1,1))
plt.ylim((-5,5))


plt.grid(True)
plt.title("YOut and YTraining comparison")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.show()


















