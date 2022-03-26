import stdio
import sys

# Accept weight (float) and height (float) as command-line arguments.
weight = float(sys.argv[1])
height = float(sys.argv[2])

# Set bmi to weight divided by square of height.
bmi = weight / (height * height)

# Write bmi to standard output.
stdio.writeln(bmi)

# initially did weight / height * height
# but added parenthesis between height * height
