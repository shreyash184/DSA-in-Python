def helper(nums):
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
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        return max(helper(nums[:len(nums)-1]), helper(nums[1:])) 