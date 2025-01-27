#Author: TEJA SUDHASHREE DEVAGUPTAPU
#Date: 24-01-2025
# A.0.4: Is it a prime number?

number = int(input('Enter the number:'))
def prime_num(n):

    if n<= 1:
        return False
    for i in range(2, int(n-1)+1):
        if n % i == 0:
            return False
    return True
if prime_num(number):
    print(number,"is a prime number")
else:
    print(number, "is not a prime number")