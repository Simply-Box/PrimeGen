# This code generates primes up to the scope nummber and currently prints the nummber of primes

import numpy as np

# Variabler
antalP = 0
scope =  100 #100_000_000

# True == Prime, False == No Prime
lis = np.full(scope, True)
lis[0] = False
lis[1] = False

for i in range(2, scope):
    # If prime: Make multiples of i False
    if lis[i]:
        antalP+=1
        # Uncomment code if you want to find the 10001:st prime nummber
        #if antal == 10001:
        #    print(i)
        for j in range(i*2, scope, i):
            lis[j] = False

print(antalP)
