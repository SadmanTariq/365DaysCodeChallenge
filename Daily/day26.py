def find_prime(n: int) -> int:
    primes = [1, 2]

    while n > len(primes):
        potential_prime = primes[-1] + 1
        i = 1
        while i < len(primes):
            if potential_prime % primes[i] == 0:
                i = 1
                potential_prime += 1
            else:
                i += 1
        primes.append(potential_prime)

    return primes[n - 1]


print(find_prime(3))