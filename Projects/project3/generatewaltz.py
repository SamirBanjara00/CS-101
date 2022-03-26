import stdarray
import stdrandom
import stdio

# create array for both minuet and trio
minuet = stdarray.create2D(11, 16)
for i in range(0, 11):
    for j in range(0, 16):
        # reads  data document and put it within minuet
        minuet[i][j] = stdio.readInt()

trio = stdarray.create2D(6, 16)
for i in range(0, 6):
    for j in range(0, 16):
        trio[i][j] = stdio.readInt()


for i in range(0, 16):
    die1 = stdrandom.uniformInt(0, 6)
    die2 = stdrandom.uniformInt(0, 6)
    die3 = die1 + die2
    stdio.write(str(minuet[die3][i]))
    stdio.write(' ')

for i in range(0, 16):
    die = stdrandom.uniformInt(0, 6)
    stdio.write(str(trio[die][i]))
    stdio.write(' ')
stdio.writeln(' ')
