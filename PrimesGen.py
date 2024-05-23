# This code generates primes up to the scope nummber (all prime nummbers below the scope) and currently prints the nummber of primes
import numpy as np

nummberOfPrime = 0
scope =  100 #100_000_000

# True == Prime, False == No Prime
list = np.full(scope, True)
# 0 and 1 are not prime
list[0] = False
list[1] = False

for i in range(2, scope):
    # If i prime: Make multiples of i False
    if list[i]:
        for j in range(i*2, scope, i):
            list[j] = False
        nummberOfPrime+=1
        # Uncomment code if you want to for example find the 10001:st prime nummber, print all primes and so on
        #if nummberOfPrime == 10001:
        #    print(i)

print(nummberOfPrime)
