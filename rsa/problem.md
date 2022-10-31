If you're not familiar with some of the background topics for today's challenge, you'll need to do some reading on your own. Feel free to ask if you're lost, but try to figure it out yourself first. This is a difficult challenge.

Implement the RSA key generation process following the specification on Wikipedia, or some other similar specification. Randomly generate 256-bit or larger values for p and q, using the Fermat primality test or something similar. Use e = 65537. Provide functions to encrypt and decrypt a whole number representing a message, using your selected n. Verify that when you encrypt and then decrypt the input 12345, you get 12345 back.

It's recommended that you use a large-number library for this challenge if your language doesn't support big integers.

#Links

https://en.wikipedia.org/wiki/RSA_%28cryptosystem%29#Key_generation
https://en.wikipedia.org/wiki/Primality_test#Fermat_primality_test
