def main(num_digits):
    fibonacci_sequence = [0, 1]
    found = False
    index = 1

    while not found:
        next_number = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_number)
        index += 1

        if len(str(fibonacci_sequence[-1])) == num_digits:
            print(fibonacci_sequence[-1])
            found = True

    print(index)

main(1000)
