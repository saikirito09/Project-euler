def main():
    total_sum = 0

    for i in range(1, 1001):
        total_sum += i ** i
    
    last_ten_digits = str(total_sum)[-10:]
    
    return last_ten_digits

if __name__ == '__main__':
    print(main())
