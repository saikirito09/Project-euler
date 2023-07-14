def is_prime(number):
    if number == 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

def main():
    primes = []
    current_number = 1
    
    while len(primes) != 10001:
        if is_prime(current_number):
            primes.append(current_number)
        current_number += 1
    
    return primes[-1]

if __name__ == '__main__':
    print(main())
