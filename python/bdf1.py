import math
import numpy as np

def feval(funcName, *args):
    return eval(funcName)(*args)


def mult(vector, scalar):
    newvector = [0]*len(vector)
    for i in range(len(vector)):
        newvector[i] = vector[i]*scalar
    return newvector


def backwardEuler(func, yinit, x_range, h):
    numOfODEs = len(yinit)
    sub_intervals = int((x_range[-1] - x_range[0])/h)

    x = x_range[0]
    y = yinit

    xsol = [x]
    ysol = [y[0]]

    for i in range(sub_intervals):
        yprime = feval(func, x+h, y)

        yp = mult(yprime, (1/(1+h)))

        for j in range(numOfODEs):
            y[j] = y[j] + h*yp[j]

        x += h
        xsol.append(x)

        for r in range(len(y)):
            ysol.append(y[r])  # Saves all new y's

    return [xsol, ysol]


def test(t, y):
    '''
    We define our ODEs in this function.
    '''
    dy = [0] * len(y)
    dy[0] = - 0.3 * y[0]
    return dy


h = 1e-3
x = [0.0, 10.0]
yinit = [5.0]


[ts, ys] = backwardEuler('test', yinit, x, h)
np.savetxt('data/py_bdf1.csv', np.column_stack((np.array(ts), np.array(ys))), fmt="%f", delimiter=",")

