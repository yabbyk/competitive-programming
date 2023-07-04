class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        indices = []
        sortedNums = sorted(nums)
         
        for k, num in enumerate(sortedNums):
            if num == target:
                indices.append(k)
        return indices
solution = Solution()
nums = [1,2,5,2,3]
target = 2
indices = solution.targetIndices(nums,target)
print(indices)

         
    
