import stdio
import sys
import math

# input
n = int(sys.argv[1])

# store variable
a = 1
b = 0
c = 0
d = 0

# 4 nested while fucntions
while 1 <= a * a * a <= n:
    # used stdio.write() to organize
    stdio.write()
    # used math.pow because it was easier for me.
    while a + 1 <= b * b * b <= n - math.pow(a, 3):
        stdio.write()
        while a + 1 <= c * c * c <= n:
            stdio.write()
            while c + 1 <= d * d * d <= n - math.pow(c, 3):
                if math.pow(a, 3) + math.pow(b, 3) == math.pow(c, 3) + math.pow(d, 3):
                    stdio.writeln(math.pow(a, 3) + math.pow(b, 3) + '=' + a + '^3 +' + b + '^3=' + c + '^3+' + d + '^3')
            d += 1
        c += 1
    b += 1
a += 1
# set incriments for respective while body.
