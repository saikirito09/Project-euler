def main():
    for i in range(1, 1000):
        for j in range(i, 1000):
            k = 1000 - i - j
            if i**2 + j**2 == k**2:
                return i * j * k

if __name__ == '__main__':
    print(main())
