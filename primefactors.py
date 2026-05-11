import math

def prime_factors(n):
    factors = []
    
    # 1. Divide n by 2 as many times as possible
    while n % 2 == 0:
        factors.append(2)
        n //= 2
        
    # 2. n must be odd now. Loop from 3 up to sqrt(n)
    # We use step=2 to only check odd numbers
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        # While i divides n evenly, keep dividing
        while n % i == 0:
            factors.append(i)
            n //= i
            
    # 3. If n is still > 2, the remaining n is prime
    if n > 2:
        factors.append(n)
        
    return factors