import math

import scipy.special as sp

EPS = math.pow(10,-13)
def bessel_zeroes(n):
    a = 0.0
    b = 0.0
    while sp.spherical_jn(n, a, derivative=False) <= 0 :
        a = a+1.0
    b = a+1.0

    while sp.spherical_jn(n, b, derivative=False) >= 0 :
        b = b+1.0

    c = a

    old_b=b
    while (b-a)>=EPS :
        c = (a+b)/2;

        if sp.spherical_jn(n, c, derivative=False) == 0:
            break
        elif sp.spherical_jn(n, c, derivative=False) * sp.spherical_jn(n, a, derivative=False) <0 :
            b = c
        else:
            a=c
    print("Prva nula za n = {} je : ".format(n))
    print('%.12f'%c)

    a=old_b
    b=a+1.0
    while sp.spherical_jn(n, b, derivative=False) <= 0 :
        b = b+1.0

    while (b - a) >= EPS:
        c = (a + b) / 2;

        if sp.spherical_jn(n, c, derivative=False) == 0:
            break
        elif sp.spherical_jn(n, c, derivative=False) * sp.spherical_jn(n, a, derivative=False) < 0:
            b = c
        else:
            a = c
    print("Druga nula za n = {} je : ".format(n))
    print('%.12f' % c)





if __name__ == '__main__':
    bessel_zeroes(1)
    bessel_zeroes(2)