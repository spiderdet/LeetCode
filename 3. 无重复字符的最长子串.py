from typing import List, Dict, Tuple
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right, dic, max_len, length = 0, 0, {}, 0, 0
        while left < len(s):
            while right<len(s) and s[right] not in dic.keys():
                dic[s[right]] = 1
                max_len = max(max_len, right+1-left)
                right+=1
            if s[left] in dic:
                del dic[s[left]]
            left+=1
        return max_len

if __name__ == "__main__":
    # test()
    sol = Solution()
    print(sol.lengthOfLongestSubstring("abcabcbb"))