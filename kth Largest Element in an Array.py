class Solution:
    def kthLargestNumber(self, nums: list[str], k: int) -> str:
        order = sorted(map(int,nums), reverse = True)
        kth_largest = str(order[k-1])
        return kth_largest

solution = Solution()
nums = ['3', '6', '7', '10']
k = 4
kth_max = solution.kthLargestNumber(nums, k)
print(kth_max)
