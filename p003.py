def main(n):
    divisor = 2
    while divisor * divisor < n:
        while n % divisor == 0:
            n //= divisor
        divisor += 1
    return n

print(main(600851475143))