def exponential_growth(n, factor, days):
    growth_sequence = [n]
    current_followers = n

    for _ in range(days):
        current_followers *= factor
        growth_sequence.append(current_followers)
    return growth_sequence 
        
    
