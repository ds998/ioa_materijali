# coding=utf-8
# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import numpy as np
import scipy.special as sp
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

def plot_bessel():
    # Use a breakpoint in the code line below to debug your script.
    #print("Hi, {0}".format(name))  # Press ⌘F8 to toggle the breakpoint.
    x = np.linspace(0, 20, 1000)
    for v in range(1, 3):
        plt.plot(x, sp.spherical_jn(v, x, derivative=False), label='n = '+str(v))
    plt.xlim((0, 20))
    plt.ylim((-0.2, 0.5))

    plt.grid(True)
    plt.title("Spherical Bessel Function")
    plt.xlabel("x")
    plt.ylabel("jn(x)")
    plt.legend()
    plt.show()




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    plot_bessel()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
