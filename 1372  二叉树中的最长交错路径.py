import queue

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def longestZigZag(self, root: TreeNode) -> int:

        def longest(node, dir):
            if not node:
                return 0
            if dir == 1:
                return 1 + longest(node.right, 0)
            else:
                return 1 + longest(node.left, 1)

        return max(longest(root, 0), longest(root, 1)) -1  # 这样问题在于不是从root出发的最长交叉路径没法得到


def create_tree(list):
    q = queue.Queue()
    if list[0] is None:
        print("empty")
    else:
        root = TreeNode(1)
        q.put(root.left)
        q.put(root.right)
    for i in list[1:]:
        print(i)
        if i is None:
            q.get(False)
        else:
            newNode = TreeNode(1)
            branch = q.get(False)
            branch = newNode
            q.put(newNode.left)
            q.put(newNode.right)
    return root

def print_tree(root):
    q = queue.Queue()
    q.put(root)
    q.put(0)
    flag = False
    while True:
        node = q.get(False)
        if node == 0:
            if flag:
                print("") #换行
                q.put(0)
                flag = False
                continue
            else:
                break
        if node is None:
            print("n", end="")
            q.put(None)
            q.put(None)
        else:
            print(node.val, end="")
            flag = True
            q.put(node.left)
            q.put(node.right)

# root = create_tree([1,None,1,1,1,None,None,1,1,None,1,None,None,None,1,None,1])
root = TreeNode(1)
root.right = TreeNode(1)
root.left = TreeNode(1)
root.left.right = TreeNode(1)
root.left.right.right = TreeNode(1)
root.left.right.left = TreeNode(1)
root.left.right.left.right = TreeNode(1)
print("###################")
print_tree(root)
sol = Solution()
print("\n$$$$$$$$")
print(sol.longestZigZag(root))