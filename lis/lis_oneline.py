# type: ignore
# sourcery skip: swap-if-expression

# solution:
[(it := __import__("itertools")), (longest_increasing_subsequence := lambda nums: [(seq := [nums[0]]), (ms := 1), [[(seq.append(num)), (ms := ms + 1)] if num > seq[-1] else [(left := 0), (right := len(seq) - 1), [[[(mid := (left + right) // 2), (left := mid + 1) if seq[mid] < num else (right := mid)]for _ in it.takewhile(lambda _: left < right, it.count())], (seq.__setitem__(left, num))]]for num in nums[1:]], ms][-1] if nums else 0)] # noqa


def main() -> None:
    print(longest_increasing_subsequence([10, 9, 2, 5, 3, 7, 101, 18]))


if __name__ == "__main__":
    main()
