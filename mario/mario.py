width = int(input("Enter width: "))
char = "#"

# First one
for i in range(width):
    print(" " * (width - i) + char * (i + 1))

print()

# second one
for i in range(width):
    print(" " * (width - i) + char * (i + 1), end="")
    print(" ", end="")
    print(char * (i + 1) + " " * (width - i))
