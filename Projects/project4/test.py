import stdio
import stdrandom


def primes(lo, hi):
    prime_list = []
    for p in range(lo, hi):
        prime = True
        if p <= 2:
            prime = False
        i = 2
        for i in range(2, p):
            if p % i == 0:
                prime = False
        if prime:
            prime_list += [p]
    return prime_list
"""
 def _primes(lo, hi):
   li = []
    for p in range(lo, hi):
       prime = True
        if p < 2:
            prime = False
        i = 2
        while i <= p // i:
            for i in range(2, p):
                if p % i == 0:
                    prime = False
            if prime:
                li += [p]
    return li
    
"""

"""
def _sample(a, k):
    b = []
    for v in a:
        b += [v]

    for i in range(1, int(len(a)) - 1):
        r = stdrandom.uniformInt(0, int(len(a)))
        temp = b[r]
        b[r] = b[i]
        b[i] = temp
        b += [i]
    return b[:k]
"""





print(primes(50,100))

