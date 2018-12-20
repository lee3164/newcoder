# coding=utf-8

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    """
    根据一棵树的前序遍历与中序遍历构造二叉树。

注意:
你可以假设树中没有重复的元素。

例如，给出

前序遍历 preorder = [3,9,20,15,7]
中序遍历 inorder = [9,3,15,20,7]
返回如下的二叉树：

    3
   / \
  9  20
    /  \
   15   7

    前序的第一个节点一定是根节点，依次划分成左子树和右子树的前序中序，递归即可
    """
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """

        def helper(i, j, p, q):
            if i > j:
                return None
            root = TreeNode(preorder[i])
            root_inorder_idx = inorder.index(preorder[i])
            left_num = root_inorder_idx - p
            root.left = helper(i + 1, i + left_num, p, root_inorder_idx - 1)
            root.right = helper(i + left_num + 1, j, root_inorder_idx + 1, q)
            return root

        l = len(inorder) - 1
        return helper(0, l, 0, l)


if __name__ == '__main__':
    print Solution().buildTree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7])
