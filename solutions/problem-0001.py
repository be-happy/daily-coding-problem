# Daily Coding Problem: Problem #1 [Easy]
#
# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
# For example, given `[10, 15, 3, 7]` and `k` of `17`, return `true` since `10 + 7` is `17`.
# Bonus: Can you do this in one pass?


# Time: O(n^2), where n is len(nums)
# Space: O(1)

def pair1(nums, k):
    n = len(nums)
    for i in range(n):
        num = nums[i]
        compliment = k - num
        for j in range(n):
            if i!=j and nums[j]==compliment:
                return True
    return False

# Time: O(n*log(n)), where n is len(nums)
# Space: O(1)

def pair2(nums, k):
    nums.sort()
    l = 0
    r = len(nums) - 1
    while l<r:
        if nums[l] + nums[r] == k:
            return True
        elif nums[l] + nums[r] < k:
            l += 1
        else:
            r -= 1
    return False

# Time: O(n), where n is len(nums)
# Space: O(n), where n is len(nums)

def pair3(nums, k):
    h = {}
    for n in nums:
        m = k-n
        if m in h:
            return True
        else:
            h[n] = 1
    return False

# assert pair1([10, 15, 3, 7], 17) == True
# assert pair2([10, 15, 3, 7], 17) == True
# assert pair3([10, 15, 3, 7], 17) == True
