import sys
import math
import print as draw


def fonction(x, n):
    a = 0
    result = 1
    while (a <= n):
        if (x != 0):
            result *= math.sin(x / ((2 * a) + 1)) / (x / ((2 * a) + 1))
        a += 1
    return (result)


def trapezoidal(n):
    counter = 1
    result = 0.0
    h = 5000.0 / 10000.0
    while (counter < 10000):
        result += fonction(counter * h, n)
        counter += 1
    result = 0.25 * (fonction(0, n) + fonction(5000, n) + 2 * result)
    draw.print_trap(result, n)

def simpson(n):
    counter = 1
    result1 = 0.0
    h = 5000.0 / 10000.0
    while (counter < 10000):
        result1 += fonction(counter * h, n)
        counter += 1
    result2 = 0.0
    counter = 0
    while (counter < 10000):
        result2 += fonction(counter * h + (h * 0.5), n)
        counter += 1
    result = 5000.0 / 60000.0 * (fonction(0, n) + fonction(5000, n) + 2 * result1 + 4 * result2)
    draw.print_homer(result, n)




def letsdothis(start):
    draw.print_mid(1, 2)
    print()
    trapezoidal(start)
    print()
    simpson(start)

def main(argv):
    if (len(argv) == 1):
        try:
            a = int(argv[0])
        except ValueError:
            sys.exit(84)
        letsdothis(a)
        sys.exit(0)
    else:
        sys.exit(84)