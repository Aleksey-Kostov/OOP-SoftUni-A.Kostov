def get_primes(numbers: list):
    for number in numbers:
        if number < 2:
            continue
        for i in range(2, number):
            if number % i == 0:
                break
        else:
            yield number
