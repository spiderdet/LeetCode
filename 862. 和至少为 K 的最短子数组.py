from typing import List, Dict, Tuple
class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        left, right, sum = 0,0,0
        min_length = len(nums)+1
        while right < len(nums):
            sum += nums[right]
            right += 1
            while left < right:
                if sum >= k and right - left < min_length:
                    min_length = right - left
                sum -= nums[left]
                left +=1
        if min_length == len(nums)+1:
            min_length = -1
        return min_length

if __name__ == "__main__":
    # test()
    sol = Solution()
    print(sol.shortestSubarray([84,-37,32,40,95],167))