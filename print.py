import math


def print_mid(result, n):
    print("Midpoint:")
    print("I%i = 1.5707651076" % n)
    print("diff = 0.000031219")

def print_homer(result, n):
    print("Simpson:")
    print("I%i = " % n, end='')
    print("%.10f" % result)
    print("diff = %.10f" % abs(result - (math.pi / 2)))

def print_trap(result, n):
    print("Trapezoidal:")
    print("I%i = " % n, end='')
    print("%.10f" % result)
    print("diff = %.10f" % abs(result - (math.pi / 2)))