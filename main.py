from primesCPlus import calculatePrimesCPlus
from primesPython import calculatePrimesPython
from primesC import calculatePrimesC


def compareByTens(power):
    factor = 1
    mult = 10
    for i in range(1, power+1):
        factor *= mult
        print("\nTime to calculate " + str(factor) + " prime intgeters.")
        calculatePrimesC(factor)
        calculatePrimesCPlus(factor)
        calculatePrimesPython(factor)



if __name__ == '__main__':
    compareByTens(6)
