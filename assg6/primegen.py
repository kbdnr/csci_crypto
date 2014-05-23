#In order to accomodate for proper memory use, prime generation is done
#in this file.

#Sieve of Eratosthenes
def primes_sieve2(limit):
  a = [True] * limit      # Initialize the primality list
  a[0] = a[1] = False

  for (i, isprime) in enumerate(a):
    if isprime:
      yield i
      for n in range(i*i, limit, i):     # Mark factors non-prime
        a[n] = False
  return a

primes = primes_sieve2(217799465)
