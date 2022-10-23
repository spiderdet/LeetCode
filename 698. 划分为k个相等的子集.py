from typing import List, Dict, Tuple
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        # @cache
        # cache = dict()  # 手动实现记忆化单元
        # print(nums)
        total = sum(nums)
        if total % k != 0:
            return False
        n = len(nums)
        target = total // k  # 目标非空子集的和
        nums.sort(reverse=True)  # 升序排列
        # print(nums)
        if nums[0] > target:  # 最大值超过目标子集和，无法划分
            return False

        def dfs(state, start_j, summ):
            # print(state, summ)
            # if (state, summ) in cache:  # 从记忆中直接读取
            #     print("in cache", state, summ, cache[(state, summ)])
            #     return cache[(state, summ)]

            if state == (1 << n) - 1:  # 所有整数均已划分，结束递归，并返回True
                # cache[(state, summ)] = True
                return True
            flag = False # flag = False代表这是当前桶第一次尝试加数，这里的优化原理是如果当前桶是空的，那
            #第一个可选数必须放在该桶里，否则最后一定不能划分，不如早点return
            last_not_choose_j = -1 # 这个优化对应的是桶在选数的时候，上一个数和当前要选的数相同就跳过
            for j in range(start_j,n):# 用start_j来保证一个桶内的dfs不会走回头路，新桶则重新开始
                if flag and summ==0:  # nums已升序排列，当前数字不行，后续肯定也不行
                    break
                if summ + nums[j] > target or \
                        (last_not_choose_j>-1 and nums[last_not_choose_j]==nums[j]):
                    continue
                if state & (1 << j) == 0:  # nums[i]暂未被划分
                    flag = True # 只要分了数据就是true
                    next_state = state + (1 << j)  # 划分nums[i]
                    next_summ = (summ + nums[j]) % target
                    if next_summ == 0:
                        next_start_j = 0
                        flag = False#只有桶清空的时候才会设flag=false
                    else:
                        next_start_j = j+1
                    last_not_choose_j = j
                    if dfs(next_state,next_start_j,next_summ):  # 划分nums[i]能形成有效方案
                        # cache[(state, summ)] = True  # 加入记忆化单元【避免后续重复计算】
                        return True

            # cache[(state, summ)] = False  # 加入记忆化单元【避免后续重复计算】
            return False
        return dfs(0,0, 0)

    # def canPartitionKSubsets(self, nums, k):
    #     """
    #     :type nums: List[int]
    #     :type k: int
    #     :rtype: bool
    #     每个元素可能放到k个不同的子集里面
    #     """
    #     # 回溯，时间复杂福O(k^n)，每个元素可以选一个桶放入，关键在于树层去重剪枝
    #     sums = sum(nums)
    #     n = len(nums)
    #     if sums % k != 0:
    #         return False  # 不能整除直接返回
    #     else:
    #         # 1.1 能整除先求target，设置初始数组
    #         target = sums // k
    #         nums.sort(reverse=True)
    #         print(nums)
    #         path = [target] * k  # 初始为target
    #         if nums[0] > target: return False
    #
    #         def huisu(startIndex):
    #             # 1.1 输入startIndex对应当前数组索引
    #             # 1.2 返回条件，当数组遍历完时
    #             if startIndex > n - 1:
    #                 return True
    #             # 1.3 遍历不同的桶
    #             for i in range(k):
    #                 if path[i] - nums[startIndex] >= 0:
    #                     # 1.4.1 剪枝1：只有相减后path[i]>=0才能继续
    #                     if i > 0 and path[i] == path[i - 1]:
    #                         # 1.4.2 剪枝2：关键剪枝，树层去重，当前层path[i]和path[i-1]相等时直接跳过，为重复计算
    #                         continue
    #                     path[i] -= nums[startIndex]
    #                     if huisu(startIndex + 1):
    #                         return True
    #                     path[i] += nums[startIndex]
    #             return False
    #
    #         return huisu(0)


if __name__ == "__main__":
    # test()
    sol = Solution()
    print(sol.canPartitionKSubsets([4, 3, 2, 3, 5, 2, 1],4))