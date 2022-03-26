import stdio
import sys

# inputs
n = int(sys.argv[1])

# nested for function
for i in range(2, n):
    total = 0
    for j in range(1, i // 2):
        if i % j == 0:
            total = total + j
        if total == i:
            stdio.writeln(i)
#output
stdio.writeln(i)
