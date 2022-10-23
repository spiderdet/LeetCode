from typing import List, Dict, Tuple
from utils import timer
import heapq

def test():
    heap = [1,4,2,3,6,9]
    heapq.heappush(heap,5)
    print(heapq.nlargest(3,heap))

class Solution:
    @timer
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        left, right = 0, 0
        window, max_list, res = [], [], []
        while right < len(nums):
            # window.append(right)
            # 增加了末位，更新window内数据
            while len(max_list) > 0 and nums[max_list[-1]] <= nums[right]:
                max_list.pop()
            max_list.append((right))
            right+=1
            if right - left >= k:
                res.append(nums[max_list[0]])
                if max_list[0] == left:
                    max_list.pop(0)
                # 去掉首位，更新window数据
                # window.pop(0)
                left+=1
        return res

    @timer
    def maxSlidingWindow_for(self, nums: List[int], k: int) -> List[int]:
        left, right = 0, 0
        max_list, res =  [], []
        for right,right_num in enumerate(nums):
            # 增加了末位，更新window内数据
            while max_list and nums[max_list[-1]] <= right_num:
                max_list.pop()
            max_list.append((right))
            if right-1 - left >= k:
                res.append(nums[max_list[0]])
                if max_list[0] == left:
                    max_list.pop(0)
                # 去掉首位，更新window数据
                left += 1
        return res
    @timer
    def maxSlidingWindow2(self, nums, k):
        if not nums or k == 0:
            return None
        if k == 1:
            return nums
        window, result = [], []  # window装下标而不是nums里的值，为了防止右侧因为小于待加入值pop掉后，数不清window里现在有几个元素，从而搞不清是不是应该pop最左边元素,见下面注释#####
        for i, num in enumerate(nums):
            # 加入window前，右边如果有比它小的，就从右边pop，没有之后再加入
            if i >= k and i - window[0] >= k:  #####if len(window) == k: 有上面说的bug
                # 另外，上面这句只有在i>=k才可能出现，可以避免window[0]不存在的情况
                window.pop(0)
            while window and nums[window[-1]] <= num:
                window.pop()
            window.append(i)

            # 如果i>=k-1，输出window最左值
            if i >= k - 1:
                result.append(nums[window[0]])
        return result

if __name__ == "__main__":
    # test()
    sol = Solution()
    # print(sol.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3))
    k = 26779
    with open("239.txt","r") as f:
        list1 = list(map(int, f.read().strip().split(",")))
    print(len(list1))
    sol.maxSlidingWindow(list1,k)
    sol.maxSlidingWindow_for(list1,k)
    sol.maxSlidingWindow2(list1,k)
