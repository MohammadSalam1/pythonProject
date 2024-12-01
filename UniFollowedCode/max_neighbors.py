def max_neighbors(numbers):
    if len(numbers) < 2:
        return None  # Om listan har färre än två element, returnera None
    return max(numbers[i] + numbers[i+1] for i in range(len(numbers) - 1))

# Exempelanvändning
result = max_neighbors([9, 4, 13, 7, 8, 5])
print(result)  # Output: 20
