from typing import List, Dict, Tuple
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def eligibleWindow(need: Dict, windowDict: Dict) -> bool:
            for key, value in need.items():
                if windowDict.get(key,0)< value:
                    return False
            return True
        need, windowDict = {}, {}
        for i in t:
            need[i] = need.get(i,0) + 1
        left, right, window = 0, 0, ""
        minLength = len(s)+1
        minWindow = ""
        while right < len(s):
            window += s[right]
            windowDict[s[right]] = windowDict.get(s[right],0) + 1
            right += 1
            print(window)
            #如果含了t所有字母，再缩小窗口，不断缩小至最小，记录此时子串和长度
            while eligibleWindow(need,windowDict):
                if len(window) < minLength:
                    minLength = len(window)
                    minWindow = window
                    print(minLength, minWindow)
                window = window[1:]
                windowDict[s[left]] -= 1
                left+=1

        return minWindow


if __name__ == "__main__":
    # test()
    sol = Solution()
    print(sol.minWindow("ADOBECODEBANC","ABC"))