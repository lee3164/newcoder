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
    将一个按照升序排列的有序数组，转换为一棵高度平衡二叉搜索树。

本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1。

示例:

给定有序数组: [-10,-3,0,5,9],

一个可能的答案是：[0,-3,9,-10,null,5]，它可以表示下面这个高度平衡二叉搜索树：

      0
     / \
   -3   9
   /   /
 -10  5

    每次选中间的节点做根一定是 平衡的
    """
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """

        def helper(i, j):
            if i > j:
                return None
            root_idx = (i + j) / 2
            root = TreeNode(nums[root_idx])
            root.left = helper(i, root_idx - 1)
            root.right = helper(root_idx + 1, j)
            return root

        return helper(0, len(nums) - 1)


if __name__ == '__main__':
    pass
