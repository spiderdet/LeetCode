import pysnooper


class Solution(object):
    def maxProfit0(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        n = len(prices)
        dp = [[0 for i in range(n)], [0 for i in range(n)]]  # 第一个列表代表持股0的随天数变化变化的最大利润，第二个列表代表持股1
        dp[0][0] = 0
        dp[1][0] = -prices[0]

        for i in range(n - 1):  # 递推是从第i天往第i+1天推，因此-1
            dp[0][i + 1] = max(dp[0][i], dp[1][i] + prices[i + 1])
            dp[1][i + 1] = max(dp[0][i] - prices[i + 1], dp[1][i])
        return dp[0][n - 1]

    @pysnooper.snoop()
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        if not n or n == 1 or not k:  #平凡情况
            return 0
        if k >= n // 2:  #k给的过多，相当于交易次数无限制，用之前的简易代码，防止建k数组时浪费大量空间
            return self.maxProfit0(prices)

        dp = [
            [[float('-inf')] * n for _ in range(k+1)], #####注意，是k+1，不是k，因为k的含义是已经完成的交易数，限制为k也是[0,k]双闭区间
            [[float('-inf')] * n for _ in range(k+1)]] ######另外注意炸裂[]不要多一个，3维数组就3个[]，
        dp[0][0][0] = 0
        dp[1][0][0] = -prices[0]

        for i in range(n - 1):  # 天数
            for j in range(k+1):  # 交易次数
                if dp[0][j][i] != float('-inf'):
                    if dp[0][j][i + 1] < dp[0][j][i]:  #更新，  状态转移方程详见印象笔记-编程-极客时间面试到28-最后
                        dp[0][j][i + 1] = dp[0][j][i]
                    if dp[1][j][i + 1] < dp[0][j][i] - prices[i + 1]:
                        dp[1][j][i + 1] = dp[0][j][i] - prices[i + 1]
                if dp[1][j][i] != float('-inf'):
                    if dp[1][j][i + 1] < dp[1][j][i]:
                        dp[1][j][i + 1] = dp[1][j][i]
                    if j < k: #如果交易次数达到上限，不允许卖，
                        if dp[0][j + 1][i + 1] < dp[1][j][i] + prices[i + 1]:
                            dp[0][j + 1][i + 1] = dp[1][j][i] + prices[i + 1]

        #错了 return dp[0][k][n - 1]  ######有时候不一定是最大交易次数才取到最大值！！！
        return max([dp[0][j][n-1] for j in range(k+1)])

sol = Solution()
prices = [1,2,4,2,5,7,2,4,9,0]
sol.maxProfit(4, prices)
