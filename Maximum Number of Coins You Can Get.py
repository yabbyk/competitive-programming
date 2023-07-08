class Solution:
    def maxCoins(self, piles: list[int]) -> int:
        max_num = 0
        order = sorted(piles)
        n = len(order)
        i = n-2
        while i >= n//3:
            max_num += order[i]
            i -= 2
        return max_num
    

solution = Solution()
piles = [2,4,1,2,7,8]
max_num = solution.maxCoins(piles)
print(max_num)
