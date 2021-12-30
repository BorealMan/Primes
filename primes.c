#include <stdio.h>
#include <math.h>

int isPrime(int n)
{
    if (n < 2)
    {
        return 0;
    }
    else if (n == 2)
    {
        return 1;
    }
    else
    {
        float upTo = sqrt(n);
        for (int i = 2; i <= upTo; i++)
        {
            if (n % i == 0)
            {
                return 0;
            }
        }
        return 1;
    }
}

void calculatePrimes(int max)
{
    for (int i = 2; i <= max; i++)
    {
        if (isPrime(i) == 1)
        {
            printf("%d ", i);
        }
    }
}

int main(int arg, char *argv[])
{
    calculatePrimes(atof(argv[1]));
    return 0;
}