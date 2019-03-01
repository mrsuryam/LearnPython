#enter a number as the input, the program will determine weather it
# the number is prime or not.
# if it is not prime, prints the nearest prime number
import math 
def prime(number):
    count = 0
    for i in range(2, number):
        if(number%i == 0):
            count=count+1
    if (count ==0):
        return 1
    else:
        return 0
    
if __name__ == "__main__":
    number = int(input("Enter a number: "))
    result = prime(number)
    if (result):
        print("The number is prime")
    else:
        print("The number is not a Prime, finding the nearest number")
        # prime gap: The differnece between two successive primes
        # The prime gap keeps on increasing as the number increases 
        # The officially known prime gap is 1550 which is the difference 
        # between 8,361,375,334,787,046,697	& 423,731,791,997,205,041
        # refer: https://en.wikipedia.org/wiki/Prime_gap
        primegap = 1550
        for i in range (1, primegap+1):
            result =prime(number+i)
            if (result):
                print("The nearest prime number is ", end =" ")
                print(number+i)
                break
            result=prime(number-i)
            if (result):
                print("The nearest prime number is " ,end =" ")
                print(number+i)
                break
        print("END")

        


