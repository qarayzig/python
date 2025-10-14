def two_sum(nums, b):
    a = {} 

    for i, num in enumerate(nums):
        complement = b - num 
        if complement in a:
            return [a[complement], i] 
        a[num] = i 
    return None