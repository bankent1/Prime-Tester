"""
Check probable prime
Author: Travis Banken

This program checks if a number is probably prime using Fermat's Little Theorem
"""

# evaluates expression using successive squares
def successiveSquares(a, b, n):
    prod = 1
    binRep = "{0:b}".format(b)[::-1]
    prev = a % n
    for c in binRep:
        if c == '1':
            #print(prev)
            prod = (prod * prev) % n
        prev = prev**2 % n
    return prod

def checkPrime(num):
    #x = (2**(num-1)) % num
    x = successiveSquares(2, num-1, num)
    return x == 1


def main():
    num = int(input("Enter a number: "))
    if (checkPrime(num)):
        print(f'{num} is probably prime')
    else:
        print(f'{num} is not prime')


main()

