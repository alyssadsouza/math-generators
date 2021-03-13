# -*- coding: utf-8 -*-

def genPrimes():
    ''' 
    Generates successive prime numbers via the command: next(g)
    '''
    primes = []
    prime1, prime2 = 2, 3
    
    while True:

        yield prime1
        
        primes.append(prime1)
        primes.append(prime2)
        num = prime2 + 1

        while True:
            for digit in primes:
                if num % digit == 0:
                    num += 1
                    isPrime = False
                    break
                isPrime = True
            if isPrime:
                break
                
        prime1 = prime2
        prime2 = num
g = genPrimes()