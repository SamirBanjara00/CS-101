import stdaudio
import sys

waltz = []
waltz = stdio.readAllInts()

for i in range(len(waltz)):
    if i > 32 or i < 0:
        sys.exit('A waltz must contain exactly 32 measures')

for i in waltz:
    if i < 1 or i > 176:
        sys.exit('A minuet measure must be from [1, 176]')

for i in range(waltz[15], waltz[31]):
    if i < 1 or i > 96:
        sys.exit('A trio measure must be from [1, 96]')

for i in range(len(waltz)):
    if i < 16:
        file = 'data/M' + str(waltz[i])
        stdaudio.playFile(file)
    else:
        file = 'data/T' + str(waltz[i])
        stdaudio.playFile(file)
