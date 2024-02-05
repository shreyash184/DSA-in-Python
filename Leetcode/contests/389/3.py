def func(nums, k):

    prefix = [0] * len(nums)
    prefix[0] = nums[0]
    for i in range(1, len(nums)):
        prefix[i] = prefix[i-1] + nums[i]
    
    print(prefix)
        

    s = set()
    st = set()
    max_sum = -1 * 2 ** 31 - 1

    for i in range(len(nums)):
        sum = 0
        bol = False
        if nums[i] + k in st:
            print(prefix[i], " - ", (0 if nums.index(nums[i] + k)-1 < 0 else prefix[nums.index(nums[i] + k)-1]))
            sum = prefix[i] - (0 if nums.index(nums[i] + k)-1 < 0 else prefix[nums.index(nums[i] + k)-1])
            print(sum)
            bol =  True
            if bol == True:
                max_sum = max(sum, max_sum) 
        if nums[i] - k in st:
            print(prefix[i], " - ", (0 if nums.index(nums[i] - k)-1 < 0 else prefix[nums.index(nums[i] - k)-1]))
            sum = prefix[i] - (0 if nums.index(nums[i] - k)-1 < 0 else prefix[nums.index(nums[i] - k)-1])
            print(sum)
            bol = True
            if bol == True:
                max_sum = max(sum, max_sum) 
        
        st.add(nums[i])

    return (0 if max_sum == 1 * 2 ** 31 - 1 else max_sum)

nums = [4,7,3,5,5]
k = 2
print(func(nums, k))