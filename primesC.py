import os
import subprocess
import time

def calculatePrimesC(maxPrime):
    path = os.path.join(os.getcwd(), 'a.exe')
    t1 = time.time()*1000
    data = subprocess.run([path, str(maxPrime)], capture_output=True).stdout.decode('utf-8')
    t2 = time.time()*1000

    # print(data)
    print("(C++): " + str(round(t2 - t1, 5)) + " milliseconds.")


if __name__ == '__main__':
    calculatePrimesC(200)