numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
is_prime = True

for i in numbers:

    for j in range(2, i):
        is_prime = True
        if i % j == 0:
            is_prime = False
            break

    if is_prime:
        primes.append(i)
    else:
        not_primes.append(i)

print('Простые:', primes)
print('Не простые:', not_primes)
