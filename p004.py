def main():
    palindromes = []
    
    for i in range(999, 100, -1):
        for j in range(999, 100, -1):
            product = i * j
            if str(product) == str(product)[::-1]:
                palindromes.append(product)
    
    return max(palindromes)

print(main())