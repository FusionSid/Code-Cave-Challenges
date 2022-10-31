while (start_size := int(input("Enter the starting population size: "))) < 9:
    print("nah u tripping, enter a number bigger than 9")

while start_size > (stop_size := int(input("Enter the ending population size: "))):
    print("nah u tripping, enter a number bigger than or equal to the start size")


years = 0
while start_size < stop_size:
    start_size += start_size / 3 - start_size / 4
    years += 1

print(years)
