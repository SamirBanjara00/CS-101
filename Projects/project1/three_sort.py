import stdio
import sys

# inputs
x = int(sys.argv[1])
y = int(sys.argv[2])
z = int(sys.argv[3])

# selects the largest number from list 1, that has inputs user inserted
max1 = max(x, y, z)

# selects the smallest number from list 1, that has inputs user inserted
min1 = min(x, y, z)

# arithmetic formula that calculates median from inputs.
middle = (x + y + z) - (min1 + max1)

# outputs in ascending order the smallest, middle and max
stdio.writeln(str(min1) + ' ' + str(middle) + ' ' + str(max1))
