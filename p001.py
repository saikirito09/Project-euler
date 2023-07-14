def main(n):
    total_sum = 0
    for i in range(n):
        if i % 3 == 0 or i % 5 == 0:
            total_sum += i
    return total_sum

print(main(1000))