def tsp(cities, paths, dist):
    # Create a list of indices representing the cities [0, 1, ..., n-1]
    city_indices = list(range(len(cities)))
    
    # Generate all possible travel sequences
    all_paths = permutations(city_indices)
    
    for path in all_paths:
        total_distance = 0
        # Iterate through the path to sum the distances between consecutive cities
        # We stop at len(path) - 1 because the last city has no "next" city in this path
        for i in range(len(path) - 1):
            city_a = path[i]
            city_b = path[i + 1]
            total_distance += paths[city_a][city_b]
        
        # If any path is strictly less than the distance provided, return True
        if total_distance < dist:
            return True
            
    return False

# don't touch below this line

def permutations(arr):
    res = []
    res = helper(res, arr, len(arr))
    return res

def helper(res, arr, n):
    if n == 1:
        tmp = arr.copy()
        res.append(tmp)
    else:
        for i in range(n):
            res = helper(res, arr, n - 1)
            if n % 2 == 1:
                arr[n - 1], arr[i] = arr[i], arr[n - 1]
            else:
                arr[0], arr[n - 1] = arr[n - 1], arr[0]
    return res