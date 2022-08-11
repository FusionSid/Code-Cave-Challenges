# width = int(input("Enter width: "))
width = 5
char = "quack"

print("     " * (width) + "  quaack")
for i in range(width):
    print("     " * (width - i) + char * (i + 1), end="")
    print(char * (i + 1) + " " * (width - i))
