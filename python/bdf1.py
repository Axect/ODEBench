from math import *
import numpy as np


def main():
    xs = [1., 1.]
    print(jacobian(xs, f))

def f(xs):
    t = xs[0]
    x = xs[1]
    return [t**2 * x * 3]


class Dual:
    def __init__(self, x, dx):
        self.x = x
        self.dx = dx

    def __str__(self):
        return "Dual(" + str(self.x) + ", " + str(self.dx) + ")"

    def value(self):
        return self.x

    def slope(self):
        return self.dx

    def extract(self):
        return (self.x, self.dx)

    def __neg__(self):
        return Dual(-self.x, -self.dx)
    
    def __add__(self, other):
        if isinstance(other, self.__class__):
            return Dual(self.x + other.x, self.dx + other.dx)
        elif isinstance(other, int) or isinstance(other, float):
            return Dual(self.x + other, self.dx)
        else:
            raise TypeError("unsupported operand type(s) for +: '{}' and '{}'".format(self.__class__, type(other)))

    def __sub__(self, other):
        if isinstance(other, self.__class__):
            return Dual(self.x - other.x, self.dx - other.dx)
        elif isinstance(other, int) or isinstance(other, float):
            return Dual(self.x - other, self.dx)
        else:
            raise TypeError("unsupported operand type(s) for -: '{}' and '{}'".format(self.__class__, type(other)))

    def __mul__(self, other):
        if isinstance(other, self.__class__):
            return Dual(self.x * other.x, self.x * other.dx + self.dx * other.x)
        elif isinstance(other, int) or isinstance(other, float):
            return Dual(self.x * other, self.dx)
        else:
            raise TypeError("unsupported operand type(s) for *: '{}' and '{}'".format(self.__class__, type(other)))

    def __div__(self, other):
        if isinstance(other, self.__class__):
            return Dual(self.x / other.x, (self.dx * other.x - self.x * other.dx) / other.x ** 2)
        elif isinstance(other, int) or isinstance(other, float):
            return Dual(self.x / other, self.dx)
        else:
            raise TypeError("unsupported operand type(s) for /: '{}' and '{}'".format(self.__class__, type(other)))

    def __radd__(self, other):
        return self + other

    def __rsub__(self, other):
        return other + (-self)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __rdiv__(self, other):
        if isinstance(other, self.__class__):
            return other / self
        elif isinstance(other, int) or isinstance(other, float):
            return Dual(other, 0) / self
        else:
            raise TypeError("unsupported operand type(S) for /: '{}' and '{}'").format(self.__class__, type(other))

    def __pow__(self, other):
        if isinstance(other, self.__class__):
            if other.dx == 0:
                return Dual(self.x ** other.x, (other.x * self.x ** (other.x - 1)) * self.dx)
            elif self.dx == 0:
                return Dual(self.x ** other.x, self.x ** other.x * log(self.x) * other.dx)
            else:
                return Dual(self.x ** other.x, (log(self.x) * other.dx + other.x * self.dx) / self.x * self.x ** other.x)

    def sin(self):
        return Dual(sin(self.x), cos(self.x) * self.dx)

    def cos(self):
        return Dual(cos(self.x), -sin(self.x) * self.dx)

    def tan(self):
        return Dual(tan(self.x), (1 + tan(self.x)**2) * self.dx)

    def exp(self):
        return Dual(exp(self.x), exp(self.x) * self.dx)

    def log(self):
        return Dual(log(self.x), self.dx / self.x)


def dual(x, dx):
    return Dual(x, dx)

def merge_dual(xs, dxs):
    l = len(xs)
    result = [None] * l
    for i in range(l):
        result[i] = Dual(xs[i], dxs[i])
    return result

def conv_dual(xs):
    l = len(xs)
    result = [None] * l
    for i in range(l):
        result[i] = Dual(xs[i], 0.)
    return result

def slopes(xs):
    l = len(xs)
    result = [None] * l
    for i in range(l):
        result[i] = xs[i].slope()
    return result

def jacobian(x, f):
    l = len(x)
    x_var = merge_dual(x, np.ones(l))
    x_const = conv_dual(x)
    l2 = len(f(x_const))
    J = np.zeros((l2, l))
    x_temp = x_const.copy()

    for i in range(l):
        x_temp[i] = x_var[i]
        dual_temp = f(x_temp.copy())
        slope_temp = slopes(dual_temp)
        for j in range(l2):
            J[j, i] = slope_temp[j]
        x_temp = x_const.copy()
    return J

if __name__ == '__main__':
    main()
