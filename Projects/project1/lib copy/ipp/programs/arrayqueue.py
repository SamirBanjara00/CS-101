# An iterable data type to represent the First-In-First-Out (FIFO) queue data structure.

import stdio


class ArrayQueue:
    # Initializes an empty queue.
    def __init__(self):
        self.a = []  # items in the queue

    # Returns True if this queue is empty, and False otherwise.
    def isEmpty(self):
        return len(self) == 0

    # Returns the number of items in this queue.
    def __len__(self):
        return len(self.a)

    # Adds item to the end of this queue.
    def enqueue(self, item):
        self.a.append(item)

    # Returns the item at the front of this queue.
    def peek(self):
        if self.isEmpty():
            raise Exception('Queue is empty')
        return self.a[0]

    # Removes and returns the item at the front of this queue.
    def dequeue(self):
        if self.isEmpty():
            raise Exception('Queue is empty')
        return self.a.pop(0)

    # Returns an iterator that iterates over the items in this queue.
    def __iter__(self):
        return iter(self.a)

    # Returns a string representation of this stack.
    def __str__(self):
        s = ''
        for v in self:
            s += str(v) + ', '
        s = '[' + s[:-2] + ']' if len(self) > 0 else '[]'
        return s


# Unit tests the data type.
def _main():
    queue = ArrayQueue()
    while not stdio.isEmpty():
        item = stdio.readString()
        if item != '-':
            queue.enqueue(item)
        elif not queue.isEmpty():
            stdio.write(str(queue.dequeue()) + ' ')
    stdio.writeln()
    stdio.writeln(str(len(queue)) + ' items left in the queue')
    stdio.writeln(queue)


if __name__ == '__main__':
    _main()
