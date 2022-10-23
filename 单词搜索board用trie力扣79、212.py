import pysnooper
#答案都是board用dfs，words用字典树，我希望board装成字典树，这样以后的word都能拿进去看.
#字典树和普通树的区别，如果有共同前缀可以合并在一起，或者说如果不在乎经过什么路径到达，只检验能否到达，就可以用字典树
#这么做的问题在于大部分时间用于建立board的字典树，如果words列表不大而board很大时，时间复杂度太高！不如传统的board用dfs，words用字典树
#7*7的board就跑炸了
class Solution(object):
    def exist(self, board, word):
        #@pysnooper.snoop()
        def createTrie():
            def available(i, j, visited):
                choices = []
                if i - 1 >= 0 and (i - 1, j) not in visited:
                    choices.append((i - 1, j))
                if i + 1 < y and (i + 1, j) not in visited:
                    choices.append((i + 1, j))
                if j - 1 >= 0 and (i, j - 1) not in visited:
                    choices.append((i, j - 1))
                if j + 1 < x and (i, j + 1) not in visited:
                    choices.append((i, j + 1))
                return choices

            #@pysnooper.snoop()
            def dfs(dic,i,j,visited):
                choices = available(i,j,visited)
                if not choices: #递归基
                    return
                for (newi,newj) in choices:
                    c = board[newi][newj]
                    subdic = dic.setdefault(c, {})  # 接下来就是在subdic里加键值对
                    visited.append((newi, newj))
                    dfs(subdic,newi,newj,visited)
                    visited.remove((newi,newj))
                return

            dic = {}
            if y==0 or x==0:
                return dic
            visited = []
            for i in range(y):
                for j in range(x):
                    c = board[i][j]
                    subdic = dic.setdefault(c, {})  # 接下来就是在subdic里加键值对
                    visited.append((i, j))
                    dfs(subdic, i, j, visited)
                    visited.remove((i, j))
            return dic

        def showTrie(root):
            def show(root_value, subdic):
                #print(root_value, [i for i in subdic])
                for i in subdic:
                    show(i, subdic[i])
            show('+', root)

        def search(root, word):
            for i in word:
                if i in root:  # i in dict 就相当于 i in dict.keys,见印象笔记-python
                    root = root[i]
                else:
                    return False
            return True

        y, x = len(board), len(board[0])
        root = createTrie()
        #showTrie(root)
        return search(root, word)


sol = Solution()
'''
board = [ 别用，会死机
    ["F","Y","C","E","N","R","D"],
    ["K","L","N","F","I","N","U"],
    ["A","A","A","R","A","H","R"],
    ["N","D","K","L","P","N","E"],
    ["A","L","A","N","S","A","P"],
    ["O","O","G","O","T","P","N"],
    ["H","P","O","L","A","N","O"]]
'''
board =[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']]

words =["poland"] #["ABCCED","SEE","ABCB"]
for word in words:
    print(word, sol.exist(board, word))

