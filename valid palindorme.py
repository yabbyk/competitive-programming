class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = " ".join(i for i in s if i.isalnum())
        return s == s[::-1]


solution = Solution()
s = "race a car"
palindrome = solution.isPalindrome(s)
print(palindrome)
