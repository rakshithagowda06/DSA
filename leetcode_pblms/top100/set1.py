def get_max_length(nums):
    if not nums:
        return 0
        
    num_set = set(nums)
    max_length = 0  # Track maximum!
    
    for num in num_set:
        if num - 1 not in num_set:  # Found a start
            length = 1
            current = num  # Use a different variable!
            
            while (current + 1) in num_set:
                length += 1
                current += 1
            
            max_length = max(max_length, length)  # Update max!
    
    return max_length