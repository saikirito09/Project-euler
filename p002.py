def main():
    fibonacci = [0, 1]
    limit_reached = False
    
    while not limit_reached:
        next_number = fibonacci[-1] + fibonacci[-2]
        fibonacci.append(next_number)
        
        if next_number > 4000000:
            fibonacci.pop()
            limit_reached = True
    
    even_sum = 0
    for num in fibonacci:
        if num % 2 == 0:
            even_sum += num
    
    return even_sum

print(main())