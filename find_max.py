def find_max(numbers):
    max_val = numbers[0]
    for num in numbers: # Iterates exactly n times
        if num > max_val:
            max_val = num
    return max_val

# If list size doubles, the time to finish roughly doubles.