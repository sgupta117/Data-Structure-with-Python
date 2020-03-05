
import math
def checkPrime(num):
    for i in range(2,int(math.sqrt(num))):
        if num % i == 0:
            return False
            break
    return True

def findCircular(N):
    # Count digits.
    count = 0
    temp = N
    res = []
    c = 0
    while (temp > 0):
        count = count + 1
        temp = temp / 10

    num = N
    while(checkPrime(num)):
        res.append(N)
        c += 1
        num = int( (num % 10) * (pow(10,count - 1)) ) + num /10

        if num == N:
            return True , res
    return False, res

def main():
    a , b = findCircular(1193)
    print(a)
    print(b)


main()