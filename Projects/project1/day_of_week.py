import stdio
import sys
# Accept int m, d, y as command-line inputs
m = int(sys.argv[1])
d = int(sys.argv[2])
y = int(sys.argv[3])

# calculates year by subtracting 14 and m, divide that by 12, then subtract that by y
year = y - (14 - m) // 12

# Calculates x by adding year to year, dividing it by 4 and year which we calculated above
# Then we would divide it again by 100 plus year, then divide by 400
x = year + year // 4 - year // 100 + year // 400

# month is calculated
month = m + 12 * ((14 - m) // 12) - 2

# dow is calculated
dow = (d + x + 31 * month // 12) % 7

stdio.writeln(dow)

# changed y0 to year, x0 to x, m0 to month, and kept dow the same.
# i do not know how to write subscripts
