class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
nums = [2, 7, 11, 15]
target = 9

solution = Solution()
print(solution.twoSum(nums, target))




# THIS PROGRAM IS FOR THE THREE SUM 
class Solution(object):
    def threeSum(self, nums):
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        return [nums[i], nums[j], nums[k]]

nums = [-1, 0, 1, 2, -1, -4]
solution = Solution()
print(solution.threeSum(nums))







# THIS PROGRAM IS FOR THE FOUR SUM
class Solution(object):
    def fourSum(self, nums, target):
        nums.sort()
        result = []
        n = len(nums)
        
        for i in range(n - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, n - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                left, right = j + 1, n - 1
                while left < right:
                    total = nums[i] + nums[j] + nums[left] + nums[right]
                    if total == target:
                        result.append([nums[i], nums[j], nums[left], nums[right]])
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        left += 1
                        right -= 1
                    elif total < target:
                        left += 1
                    else:
                        right -= 1
        return result

nums = [1000000000, 1000000000, 1000000000, 1000000000]
target = -294967296
solution = Solution()
print(solution.fourSum(nums, target))