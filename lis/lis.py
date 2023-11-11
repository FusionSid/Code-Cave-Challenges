def longest_increasing_subsequence(nums: list[int]) -> int:
    if not nums:  # nothing in array so no max
        return 0

    sequence = [nums[0]]
    max_sub = 1

    for num in nums[1:]:  # start from 1 cause we already did 1
        if num > sequence[-1]:
            sequence.append(
                num
            )  # if num is more than last in seq add to end, and update max
            max_sub += 1
            continue

        # find the index where num should be in the sequence array
        left, right = 0, len(sequence) - 1
        while left < right:
            middle = (left + right) // 2
            if sequence[middle] < num:
                left = middle + 1
            else:
                right = middle

        # update that shit to the right spot
        sequence[left] = num

    return max_sub


def main() -> None:
    assert longest_increasing_subsequence([10, 9, 2, 5, 3, 7, 101, 18]) == 4


if __name__ == "__main__":
    main()
