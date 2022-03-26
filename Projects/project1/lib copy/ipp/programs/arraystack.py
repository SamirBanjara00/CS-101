# An iterable data type to represent the Last-In-First-Out (LIFO) stack data structure.

import stdio


class ArrayStack:
    # Initializes an empty stack.
    def __init__(self):
        self.a = []  # items in the stack

    # Returns True if this stack is empty, and False otherwise.
    def isEmpty(self):
        return len(self) == 0

    # Returns the number of items in this stack.
    def __len__(self):
        return len(self.a)

    # Adds item to the top of this stack.
    def push(self, item):
        self.a.append(item)

    # Returns the item at the top of this stack.
    def peek(self):
        if self.isEmpty():
            raise Exception('Stack is empty')
        return self.a[-1]

    # Removes and returns the item at the top of this stack.
    def pop(self):
        if self.isEmpty():
            raise Exception('Stack is empty')
        return self.a.pop(-1)

    # Returns an iterator that iterates over the items in this stack.
    def __iter__(self):
        return reversed(self.a)

    # Returns a string representation of this stack.
    def __str__(self):
        s = ''
        for v in self:
            s += str(v) + ', '
        s = '[' + s[:-2] + ']' if len(self) > 0 else '[]'
        return s


# Unit tests the data type.
def _main():
    stack = ArrayStack()
    while not stdio.isEmpty():
        item = stdio.readString()
        if item != '-':
            stack.push(item)
        elif not stack.isEmpty():
            stdio.write(str(stack.pop()) + ' ')
    stdio.writeln()
    stdio.writeln(str(len(stack)) + ' items left in the stack')
    stdio.writeln(stack)


if __name__ == '__main__':
    _main()
