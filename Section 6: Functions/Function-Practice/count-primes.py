# COUNT PRIMES: Write a function that returns the number of prime numbers that exist up to and including a given number¶
# count_primes(100) --> 25
# By convention, 0 and 1 are not prime.

def count_primes(num):
    primes = [2]
    x = 3
    
    # check for 0 or 1
    if num < 2:
        return 0
    
    while x <= num:
        for y in range(3,x,2):
            if x % y == 0:
                x += 2
                break
        else:
            primes.append(x)
            x += 2
    return len(primes)