import random

def generateRandomPrime(seed):
    p=3
    primeCount = 1
    primes = [2]
    while True:
        prime = True
        for i in primes:
            if p%i == 0:
                prime = False
                continue
        if prime:
            primes.append(p)
            primeCount += 1
            if (primeCount >= seed):
                break
        p += 1
    
    return p

def generateRandomPrimes(primeSize):
    seed = 0
    seed2 = 0
    while seed == seed2:
        seed = random.randrange(35, primeSize)
        seed2 = random.randrange(35, primeSize)
    return generateRandomPrime(seed), generateRandomPrime(seed2)

def generateKeyPair(primeSize):
    p, q = generateRandomPrimes(primeSize)
    n = p*q
    lambdaN = (p-1)*(q-1)
    e = 1153
    d = 0

    while True:
        if (d*e)%lambdaN == 1:
            break
        d += 1

    return (e, n), (d, n)

def encryptString(string, public_key):
    encodedString = bytearray(string, "utf-8")
    encryptedString = list((i**public_key[0])%public_key[1] for i in encodedString)
    return encryptedString

def decryptString(encryptedString, private_key):
    decryptedString = bytearray((i**private_key[0])%private_key[1] for i in encryptedString).decode()
    return decryptedString