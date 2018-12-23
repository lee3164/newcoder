# coding=utf-8

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    """
填充它的每个 next 指针，让这个指针指向其下一个右侧节点。如果找不到下一个右侧节点，则将 next 指针设置为 NULL。

初始状态下，所有 next 指针都被设置为 NULL。

说明:

你只能使用额外常数空间。
使用递归解题也符合要求，本题中递归程序占用的栈空间不算做额外的空间复杂度。
示例:

给定二叉树，

     1
   /  \
  2    3
 / \    \
4   5    7
调用你的函数后，该二叉树变为：

     1 -> NULL
   /  \
  2 -> 3 -> NULL
 / \    \
4-> 5 -> 7 -> NUL
    """
    def connect(self, root):
        if not root:
            return
        q = [root]
        while q:
            new_q = []
            i = 0
            while i < len(q):
                if q[i].left:
                    new_q.append(q[i].left)
                if q[i].right:
                    new_q.append(q[i].right)
                if i < len(q) - 1:
                    q[i].next = q[i + 1]
                i += 1
            q = new_q


if __name__ == '__main__':
    pass
