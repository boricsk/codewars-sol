'''
Write a function that takes an integer as input, and returns the number of bits that are equal to one in the binary representation of that number. 
You can guarantee that input is non-negative.

Example: The binary representation of 1234 is 10 01 10 10 01 0, so the function should return 5 in this case

'''
#eturn (len(format(n,'b')) -1 )// 2


def count_bits(n):
    counter = 0
    while (n):
        n &= n - 1
        counter += 1
        
    return counter

count_bits(1234)

#others
def countBits(n):
    return bin(n).count("1")