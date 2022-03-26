import stdio
import sys

# accept nth order
n = int(sys.argv[1])

# assign 'F'
dragon = 'F'
nogard = 'F'

# repeats function between 1 and nth order +1.
for i in range(1, n+1):

    # reassigns
    temp = dragon
    dragon = dragon + 'L' + nogard
    nogard = temp + 'R' + nogard

# output
stdio.writeln(dragon)
