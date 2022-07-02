from typing import List, Dict, Tuple
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        def judgeWindow(need,curr):
            for key, value in need.items():
                if curr.get(key,0) != value:
                    return False
            return True
        need, curr = {}, {}
        for i in s1:
            need[i] = need.get(i,0)+1
        left, right = 0, 0
        window = ""
        while right < len(s2):
            window += s2[right]
            curr[s2[right]] = curr.get(s2[right],0)+1
            right += 1

            if right - left == len(s1) and judgeWindow(need,curr):
                return True
            elif right - left == len(s1)+1:
                window = window[1:]
                curr[s2[left]]-=1
                left+=1
                if judgeWindow(need, curr):
                    return True
        return False

if __name__ == "__main__":
    # test()
    sol = Solution()
    print(sol.checkInclusion("ab","eidbaooo"))