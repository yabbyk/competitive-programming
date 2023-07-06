class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        
        for i in range (1 ,len(nums)-1):
            avg = (nums[i-1] + nums[i+1])/2
            if avg == nums[i]:
                nums[i+1],nums[i]=nums[i],nums[i+1]
        return nums

solution = Solution()
nums =  [1,2,3,4,5]
rearranged_list = solution.rearrangeArray(nums)
print(rearranged_list)
