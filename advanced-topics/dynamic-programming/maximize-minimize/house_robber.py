def rob(nums):
    a = nums[0]
    b = max(nums[0], nums[1]) if len(nums) > 1 else 0

    if len(nums) == 1:
        return a

    if len(nums) == 2:
        return b
    c = -1
    for i in range(2, len(nums)):
        c = max(nums[i]+a, b)
        a = b
        b = c
        
    return c

print(rob([7,1,1,9]))