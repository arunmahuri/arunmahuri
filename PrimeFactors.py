def isPrime(N):
    if N>1 and all(N%i!=0 for i in range(2,N)):
        return True
    return False
def smallestPrimeFactors(N,l=[]):
    for i in range(2,N+1):
        if isPrime(i) and N%i==0:
            l.append(i)
            return smallestPrimeFactors(N//i,l)
    return l
