# What does this piece of code do?
# Answer: to find a prime number from 1 to 100 (and 1 is also included).

# Import libraries
# randint allows drawing a random number, 
# e.g. randint(1,5) draws a number between 1 and 5
from random import randint

# ceil takes the ceiling of a number, i.e. the next higher integer.
# e.g. ceil(4.2)=5
from math import ceil

#this is because if n has a factor bigger than [square root of n], there should be a factor smalle than that.
#therefore, if a factor cannot be found smaller than [square root of n], n should be a prime number


#p is asking whether the number is prime or not
p=False
#p（Boolean variables) is used to control the loop
while p==False:
    #p is True than the loop is stopped
    p=True
    #draw a integer between 1 and 100
    n = randint(1,100)
    #take square root of n and u is ceiling of the root
    #it is to find the factor of n
    u = ceil(n**(0.5))
    #to confirm whether n is a prime number
    for i in range(2,u+1):
        if n%i == 0:
            #p is False, then go another loop
            p=False
    #if we can find factors of n between 2 and u+1, choose another n
    #if the n has no factor between 2 and u+1, then n is a prime number
     
print(n)
