def mode(nums):
    modes={}
    for num in nums:
        modes[num] = modes.get(num, 0) +1

    max_appear = max(modes.values())
    
    for (num, freq) in modes.items():
        if freq == max_appear:
            return num