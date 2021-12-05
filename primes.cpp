#include <iostream>
#include <math.h>
using namespace std;

bool isPrime(int n)
{
    if (n < 2)
    {
        return false;
    }
    if (n == 2)
    {
        return true;
    }
    bool isPrime = true;
    for (int i = 2; i <= sqrt(n); i++)
    {
        if (n % i == 0)
        {
            return false;
        }
    }
    return isPrime;
}

void printPrimeReport(int currentVal, int currentPrimeCount)
{
    cout << "Primes Found Within " << currentVal << ": " << currentPrimeCount << endl;
    float r = (float)currentPrimeCount / (float)currentVal;
    cout << "Percentage of Prime Numbers: " << r << endl;
}

void calcPrimesWithReports(int n)
{
    int count = 0;
    int muliplier = 10;
    int factor = muliplier;
    for (int i = 2; i <= n; i++)
    {
        if (isPrime(i))
        {
            count++;
        }
        if (i % factor == 0)
        {
            printPrimeReport(i, count);
            factor *= muliplier;
        }
    }
}

void getPrimes(int n)
{
    for (int i = 2; i <= n; i++)
    {
        if (isPrime(i))
        {
            cout << i << " ";
        }
    }
}

int main(int argc, char *argsv[])
{
    int input = atof(argsv[1]);
    getPrimes(input);
    return 0;
}