def calculate_prime(first, second):
    list_primes = []
    for i in range(first, second + 1):
        is_prime = True
        for j in range(2, i):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            list_primes.append(i)
    return list_primes


def main():
    first = int(input("Enter first number: "))
    second = int(input("Enter second number: "))
    primes = calculate_prime(first, second)
    print(f"Prime numbers between {first} and {second} are:")
    for prime in primes:
        print(prime)


main()