import math
import stdio
import sys

# input
latitude = float(sys.argv[1])
longitude = float(sys.argv[2])

# changes var
x = longitude

# formula
y = (math.log((1 + math.sin(math.radians(latitude))) / (1 - math.sin(math.radians(latitude))))) / 2

# output
stdio.writeln(str(x) + ' ' + str(y))

# initially i had
# math.log((1 + math.degrees(math.sin(latitude))) / (1 - math.degrees(math.sin(latitude)))) / 2
# i got that by looking at math function on https://docs.python.org/3/library/math.html
# added math.radians that converted degree to radians,
# realized i was supposed to put it inside the function first, then fixed parathesis.
# ran into problem when writing print fucntion. I did not know i was supposed to put str() value,
# I recived the error
# but i added str() not sure why will ask question in Si, discussion or class
