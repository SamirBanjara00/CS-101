import stdio
import math
import sys

# accepts inputs
k = int(sys.argv[1])
c = float(sys.argv[2])
epsilon = float(sys.argv[3])

# assigns t to c
t = c

# uses condition abs(1 - c / t ** k) > epsilon to start loop
while abs(1 - c / math.pow(t, k) > epsilon):

    # f(t) defined
    ft = (math.pow(t, k) - c)

    # f'(t) defined
    ft1 = (k * math.pow(t, k-1))

    # replaces f(t) and f'(t)
    t = t - ft / ft1

# outputs std root value of t
stdio.write(t)
