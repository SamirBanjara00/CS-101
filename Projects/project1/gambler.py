import stdio
import sys

# input
n1 = int(sys.argv[1])
n2 = int(sys.argv[2])
p = float(sys.argv[3])

# probability formula
q = 1 - p

# calculation formula
p1 = (1 - (p / q) ** n2) / (1 - (p / q) ** (n1 + n2))
p2 = (1 - (q / p) ** n1) / (1 - (q / p) ** (n1 + n2))

# output
stdio.writeln(str(p1) + ' ' + str(p2))

# i get an error called TypeError: unsupported operand type(s) for +: 'float' and 'str'
# this funtion stdio.writeln((p1,p2)) only works with extra paranthesis
