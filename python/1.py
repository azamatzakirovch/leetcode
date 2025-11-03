class Solution:
    def twoSum(self, nums, target):
        length = len(nums)
        start, end = 0, 0

        for i in range(0, length - 1):
            start = i
            for j in range(i + 1, length):
                end = j
                if nums[start] + nums[end] == target:
                    return [start, end]


a = Solution()

print(a.twoSum([2,7,11,15], 9))