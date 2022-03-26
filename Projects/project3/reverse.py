import stdio

# Accept all the strings from standard input and store them in a list a.
a = stdio.readAllStrings()

n = len(a)

# Reverse a
for i in range(n // 2):
    # Iterate over half of the list a...

    # Exchange element at i in a with the element at len(a) - i - 1.
    temp = a[i]
    a[i] = a[n - 1 - i]
    a[n - 1 - i] = temp
# Write a to standard output.
for i in range(n):
    if i != n - 1:
        # If i is not the last column, write a[i] with a space after.
        stdio.write(str(a[i]) + ' ')
    else:
        # Otherwise, write the element with a newline after.
        stdio.writeln()
