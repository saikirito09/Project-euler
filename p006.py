def main(n):
    sum_of_squares = 0
    sum_of_numbers = 0
    
    for i in range(1, n+1):
        sum_of_squares += i * i
        sum_of_numbers += i
    
    return (sum_of_numbers * sum_of_numbers) - sum_of_squares

print(main(100))