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
    根据一棵树的中序遍历与后序遍历构造二叉树。

    注意:
    你可以假设树中没有重复的元素。

    例如，给出

    中序遍历 inorder = [9,3,15,20,7]
    后序遍历 postorder = [9,15,7,20,3]
    返回如下的二叉树：

    3
   / \
  9  20
    /  \
   15   7
   和 105 类似的思路，不多说了
    """
    def buildTree(self, inorder, postorder):
        def helper(i, j, p, q):
            if p > q:
                return None
            root = TreeNode(postorder[q])
            root_inorder_idx = inorder.index(postorder[q])
            left_num = root_inorder_idx - i
            root.left = helper(i, root_inorder_idx - 1, p, p + left_num - 1)
            root.right = helper(root_inorder_idx + 1, j, p + left_num, q - 1)
            return root

        return helper(0, len(inorder) - 1, 0, len(postorder) - 1)


if __name__ == '__main__':
    print Solution().buildTree([9, 3, 15, 20, 7], [9, 15, 7, 20, 3])
