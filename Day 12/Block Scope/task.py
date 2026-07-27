def is_prime(num):
    num_is_prime = True
    for divisor in range(2, num):
        if divisor == num:
            continue
        if num % divisor == 0:
            num_is_prime = False
            break
    return num_is_prime

print(is_prime(73))
print(is_prime(75))