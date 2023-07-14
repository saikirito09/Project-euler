def main():
    palindromes = []

    for i in range(1, 1000000):
        binary = str(bin(i)[2:])
        decimal = str(i)

        if binary == binary[::-1] and decimal == decimal[::-1]:
            palindromes.append(i)

    return sum(palindromes)

if __name__ == '__main__':
    print(main())
