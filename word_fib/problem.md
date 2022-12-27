Fibonacci Word

A Fibonacci word is a specific sequence of binary digits (or symbols from any two-letter alphabet). The Fibonacci word is formed via repeated concatenation in the same fashion that the Fibonacci numbers are formed via repeated addition.

Create a function that takes a number n as an argument and returns the first n elements of the Fibonacci word sequence.
Examples

```
generate_word(1) ➞ "invalid"
# if n < 2 then return "invalid".

generate_word(3) ➞ "b, a, ab"

generate_word(7) ➞ "b, a, ab, aba, abaab, abaababa, abaababaabaab"
```