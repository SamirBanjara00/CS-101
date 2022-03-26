import stdio
import sys

m = int(sys.argv[1])
d = int(sys.argv[2])
y = int(sys.argv[3])

# calculates year by subtracting 14 and m, divide that by 12, then subtract that by y
y0 = y - (14 - m) // 12

# Calculates x by adding year to year, dividing it by 4 and year which we calculated above
# Then we would divide it again by 100 plus year, then divide by 400
x0 = y0 + y0 // 4 - y0 // 100 + y0 // 400

# month is calculated
m0 = m + 12 * ((14 - m) // 12) - 2

# dow is calculated
dow = (d + x0 + 31 * m0 // 12) % 7

# if functions that determines day of week depending on dow

if dow == 0:
    stdio.writeln('Sunday')

if dow == 1:
    stdio.writeln('Monday')

if dow == 2:
    stdio.writeln('Tuesday')

if dow == 3:
    stdio.writeln('Wednesday')

if dow == 4:
    stdio.writeln('Thursday')

if dow == 5:
    stdio.writeln('Friday')

if dow == 6:
    stdio.writeln('Saturday')
