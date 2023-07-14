def main():
    n = 100
    product = 1

    while n != 2:
        product *= (n * (n - 1))
        n -= 2

    digit_sum = 0

    for digit in str(product * 2):
        digit_sum += int(digit)

    return digit_sum


if __name__ == '__main__':
    print(main())
