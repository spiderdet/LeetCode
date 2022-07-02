class Solution:
    def longestPalindrome(self, s: str) -> str:
        def findLongestSubstring(s: str, l: int, r: int) -> str:
            if r>=len(s):
                return ""
            while(l>=0 and r < len(s) and s[l]==s[r]):
                l -= 1
                r += 1
            return s[l+1:r]
        longestLength, longestS = 0, ""
        for i in range(len(s)):
            ans1 = findLongestSubstring(s,i,i)
            ans2 = findLongestSubstring(s,i,i+1)
            if len(ans1)>longestLength:
                longestLength = len(ans1)
                longestS = ans1
            if len(ans2)>longestLength:
                longestLength = len(ans2)
                longestS = ans2
        return longestS

if __name__ == "__main__":
    sol = Solution()
    print(sol.longestPalindrome("abab"))