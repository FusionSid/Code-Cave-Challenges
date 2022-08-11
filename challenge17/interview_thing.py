def longest_thing(numbers: list[int]) -> list:
    numbers = sorted(numbers)
    ans = []
    for idx, num in enumerate(numbers):
        anss = []
        current_num = num
        for j, i in enumerate(numbers[idx:]):
            if numbers[i]
    return numbers

# tests:
print(longest_thing([100, 4, 200, 1, 3, 2]))