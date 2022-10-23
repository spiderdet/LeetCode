from typing import List, Dict, Tuple
from utils import timer
class Solution:
    tag = [] #用来防止重复，a+b+c=0(a<b<c)如果重复的话，a=a',b=b'，所以用a-b作为唯一性标识
    # 其实防止重复还有个最简单的办法，就是让a不要重复，以及left++,right--时跳过所有相同的元素。
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #别忘了平凡情况！ 这里其实体现在for i in range(len(nums)-2)上了，所以还好
        nums = sorted(nums)
        res = []
        for i in range(len(nums)-2):
            # 看 [i+1:]能不能找到两数之和是-i的
            if nums[i] > 0: #有可能是[0,0,0]!所以不是大于等于，而是大于
                break
            # print(i,nums[i])
            i_res = self.twoSum(nums, i+1, -nums[i])
            if i_res:
                res += i_res
        return res
    def twoSum(self, nums: List[int], left, sum) -> List[List[int]]:
        # 从[left:]能不能找到两数之和是sum的，如果能找到，返回list，并且把-sum也放进去
        res = []
        right = len(nums)-1
        # print(nums[left:right+1])
        while left < right:
            temp_sum = nums[left]+nums[right]
            # print(left, right, temp_sum)
            if temp_sum == sum:
                if -sum - nums[left] not in self.tag:
                    res.append([-sum,nums[left],nums[right]])
                    self.tag.append(-sum-nums[left])
                left +=1
                right -=1
            elif temp_sum < sum:
                left +=1
            else:
                right -=1
        return res

if __name__ == "__main__":
    # test()
    sol = Solution()
    print(sol.threeSum([0,0,0]))