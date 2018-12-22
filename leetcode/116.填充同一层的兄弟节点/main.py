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


import copy


class Solution(object):
    """
    填充它的每个 next 指针，让这个指针指向其下一个右侧节点。如果找不到下一个右侧节点，则将 next 指针设置为 NULL。

初始状态下，所有 next 指针都被设置为 NULL。

说明:

你只能使用额外常数空间。
使用递归解题也符合要求，本题中递归程序占用的栈空间不算做额外的空间复杂度。
你可以假设它是一个完美二叉树（即所有叶子节点都在同一层，每个父节点都有两个子节点）。
示例:

给定完美二叉树，

     1
   /  \
  2    3
 / \  / \
4  5  6  7
调用你的函数后，该完美二叉树变为：

     1 -> NULL
   /  \
  2 -> 3 -> NULL
 / \  / \
4->5->6->7 -> NULL

也是递归和非递归，层次遍历可以解决很多问题，递归的方式比较难想有时
    """
    def connect2(self, root):
        if not root:
            return
        q = [root]
        while q:
            new_q = []
            i = 0
            while i < len(q):
                if q[i].left and q[i].right:
                    new_q.append(q[i].left)
                    new_q.append(q[i].right)
                if i < len(q) - 1:
                    q[i].next = q[i + 1]
                i += 1
            q = new_q

    def connect(self, root):
        if not root:
            return
        if root.left and root.right:
            root.left.next = root.right
            if root.next:
                root.right.next = root.next.left
            self.connect(root.left)
            self.connect(root.right)


if __name__ == '__main__':
    print Solution().numDistinct("babgbag", "bag")
