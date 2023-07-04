class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        
        merged = [intervals[0]]
        for i in intervals[0:]:
            if i[0] <= merged[-1][1]:
                merged[-1][1] = max(merged[-1][1],i[1])
            else:
                merged.append(i)
        return merged 
            

solution = Solution()
intervals = [[1,3],[2,6],[8,10],[15,18]]
merged_intervals = solution.merge(intervals)
print(merged_intervals)
