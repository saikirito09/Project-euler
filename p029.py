def main():
    unique_powers = set()

    for i in range(2, 101):
        for j in range(2, 101):
            power = i ** j
            unique_powers.add(power)

    return len(unique_powers)

if __name__ == '__main__':
    print(main())
