def main():
    numbers = []
    
    for i in range(2, 354295):
        digit_sum = 0
        
        for digit in str(i):
            digit_sum += int(digit) ** 5
        
        if i == digit_sum:
            numbers.append(digit_sum)
    
    return sum(numbers)

if __name__ == '__main__':
    print(main())
