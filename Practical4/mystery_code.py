# What does this piece of code do?
# Answer: to find prime numbers from 1 to 100.

# Import libraries
# randint allows drawing a random number, 
# e.g. randint(1,5) draws a number between 1 and 5
from random import randint

# ceil takes the ceiling of a number, i.e. the next higher integer.
# e.g. ceil(4.2)=5
from math import ceil

p=False
#p is used to control the loop
while p==False:
    p=True
    #draw a number between 1 and 100
    n = randint(1,100)
    #find the factor of n
    u = ceil(n**(0.5))
    #to confirm whether n is a prime number
    for i in range(2,u+1):
        if n%i == 0:
            p=False


     
print(n)
            