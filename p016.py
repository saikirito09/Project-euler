def main():
    power_of_two = 2
    for _ in range(1, 1000):
        power_of_two *= 2
    
    power_string = str(power_of_two)
    digits = list(power_string)
    digit_sum = 0
    
    for digit in digits:
        digit_sum += int(digit)
    
    return digit_sum

if __name__ == '__main__':
    print(main())
