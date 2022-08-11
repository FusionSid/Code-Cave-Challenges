Binary To ASCII Conversion

Create a function that takes a string of 1's and 0's (binary) as an argument and return the equivalent decoded ASCII text. Characters can be in the range of "00000000" to "11111111", which means every eight digits of binary input represents a single character.

    a = 01100001
    b = 01100010
    c = 01100011

If you were to combine these characters into the string "abc", the corresponding binary would be 011000010110001001100011. Use the resources tab for more info on how to approach this.
Examples

binaryConversion("010010010010000001101100011011110111011001100101001000000101010001100101011100110110100000100001") 
  ➞ "I love Tech!"

binaryConversion("001100010011001000110001001100110011000100110111") 
  ➞ "121317"

binaryConversion("010000010110110101100001011110100110100101101110011001110010000001000101011001000110000101100010011010010111010000100001") 
  ➞ "Amazing Edabit!"

Notes

If you are given an empty string as input, you must also return an empty string. Otherwise, the input will always be a valid binary string.

challenge 1/2
Interview question

This problem was asked by Microsoft.

Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

For example, given [100, 4, 200, 1, 3, 2], the longest consecutive element sequence is [1, 2, 3, 4]. Return its length: 4.

Your algorithm should run in O(n) complexity.

challange 2/2