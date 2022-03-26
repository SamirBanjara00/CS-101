import stdio
import sys

# accepts inputs p and q
p = int(sys.argv[1])
q = int(sys.argv[2])

# as long as when we divide p and q the remainder isnt 0, then p = q and q = p % p
while p % q != 0:
    p = q
    q = p % q

# output
stdio.writeln(q)
