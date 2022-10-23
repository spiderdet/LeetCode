class Solution(object):
    #result = [] #设成类内变量，本来就只有最后一层用，还得上下传参就麻烦了,但如果要设成类内变量####必须在主函数入口重新初始化
    #####否则不同的测试样例结果会累加

    def solveNQueens(self, n):
        self.result = []  ##########重要，要初始化，否则不同的测试样例结果会累积,####在此处初始化即可不用写在类里
        self.dfs2(n)
        return self.result

    def dfs(self, n, level,  res, col, summ, diff):
        if level == n: #递归基
            self.result.append(res[:])  #####重要，一定要改成res.copy() 或者res[:]否则result里的值会随res变化而变化
            return

        for i in range(n):
            if (i in col) or (i + level in summ) or (i - level in diff): #剩下可放置的列号
                continue
            s = ''
            for _ in range(n):
                if _ == i:
                    s += 'Q'
                else:
                    s += '.'
            res.append(s)             #如果在dfs参数列表上做文章就不用这样append再pop了，见dfs2
            col.append(i)
            summ.append(i + level)
            diff.append(i - level)
            self.dfs(n, level + 1,  res, col, summ, diff)
            diff.pop()
            summ.pop()
            col.pop()
            res.pop()
        return

    def dfs2(self, n, level=0,  res=[], col=[], summ=[], diff=[]):
        if level == n: #递归基
            self.result.append(res)  #####当递归是在参数列表上操作时，result.append都不用copy了
            return

        for i in range(n):
            if (i in col) or (i + level in summ) or (i - level in diff): #剩下可放置的列号
                continue
            s = ''.join(['.','Q'][x==i] for x in range(n))

            self.dfs2(n, level + 1,  res+[s], col+[i], summ+[i+level], diff+[i-level])
        return

sol = Solution()
n= 4
print(len(sol.solveNQueens(n)),sol.solveNQueens(n))