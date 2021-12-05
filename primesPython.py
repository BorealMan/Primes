import math
import time

def isPrime(n):
    if n < 2:
        return 0
    if n == 2:
        return 1
    isPrime = 1
    for i in range(2, int(math.sqrt(n))):
        if n % i == 0:
            return False
    return isPrime

def printPrimes(n):
    for i in range(2, n):
        if isPrime(i):
            # print(i, end=' ')
            pass


def calculatePrimesPython(maxPrime):
    t1 = time.time()*1000
    printPrimes(maxPrime)
    t2 = time.time()*1000

    print("(Python): " + str(round(t2 - t1, 5)) + " milliseconds.")

if __name__ == '__main__':

    calculatePrimesPython(200)
