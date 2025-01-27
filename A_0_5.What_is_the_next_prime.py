#Author: TEJA SUDHASHREE DEVAGUPTAPU
#Date: 26-01-2025
# A.0.5: What is the next prime? (loop)

number = int(input('Enter the number:')) #take input using a variable
nextprime_number = number + 1            #declare a variable for identifying next prime number greater than number given

def prime_num(n):                         #use this function to identify if a given number is prime or not
    if n <= 1:
        return False
    for i in range(2, int(n - 1) + 1):
        if n % i == 0:
            return False
    return True


def nextprime_num(n):       #function defined to identify next prime number
    while not prime_num(n): #while loop continue to verify if every number after given number is prime number or not, if not then we increment value n
        n = n + 1
    return n

if number<0:
    print("Give numbers greater than 0")
else:
    nextprime_number=nextprime_num(nextprime_number) # call the function
    print("Nearest Prime number greater than", number, "is:", nextprime_number)
