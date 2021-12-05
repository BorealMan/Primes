from primesC import calculatePrimesC
from primesPython import calculatePrimesPython


def compareByTens(power):
    factor = 1
    mult = 10
    for i in range(1, power+1):
        factor *= mult
        print("\nTime to calculate " + str(factor) + " prime intgeters.")
        calculatePrimesC(factor)
        calculatePrimesPython(factor)


if __name__ == '__main__':
    compareByTens(6)
