def is_prime(number):
    if number == 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

def main():
    prime_numbers = [num for num in range(1, 2000000) if is_prime(num)]
    return sum(prime_numbers)

if __name__ == '__main__':
    print(main())
