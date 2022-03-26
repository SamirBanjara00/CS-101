# Accepts a sequence of strings from standard input; and writes the strings in reverse order to
# standard output.

from arraystack import ArrayStack
import stdio


# Entry point.
def main():
    stack = ArrayStack()
    while not stdio.isEmpty():
        s = stdio.readString()
        stack.push(s)
    for s in stack:
        stdio.write(s + ' ')
    stdio.writeln()


if __name__ == '__main__':
    main()
