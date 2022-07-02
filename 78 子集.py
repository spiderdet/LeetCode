from typing import List, Tuple, Dict

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        length = len(nums)
        setsNum = 2 ** length
        result = []
        for i in range(setsNum):
            res = []
            bin_i = format(i, "b")
            bin_i = bin_i.rjust(length, "0")
            print(bin_i)
            for idx,j in enumerate(bin_i):
                if j == "1":
                    res.append(nums[idx])
            result.append(res)
        return result

def test():
    #测试进制转换
    print(type(bin(4)))
    print(oct(4)) #可以用python console，会更清楚类型
    print(int(4))
    print(hex(4))
    print(format(4,"b"))
    print(type(format(4,"b")))

if __name__ == "__main__":
    # test()
    sol = Solution()
    print(sol.subsets([1,2,3]))