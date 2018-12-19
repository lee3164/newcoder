# coding=utf-8

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    """
    给定两个二叉树，编写一个函数来检验它们是否相同。
    如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的。
    递归简单易懂
    非递归则是用同一种遍历算法，如前序遍历，如果发现有不同的直接return 即可
    """
    def isSameTree(self, p, q):
        if not p and not q:
            return True
        if p and q and p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        return False

    def isSameTree2(self, p, q):
        st = []
        while p or q or st:
            # 此时左子树已经到了尽头，需要遍历上一个父节点的右子树
            if not p and not q:
                p, q = st.pop()
                p, q = p.right, q.right
            elif p and q and p.val == q.val:
                st.append((p, q))
                p, q = p.left, q.left
            else:
                return False


if __name__ == '__main__':
    a = TreeNode(10)
    b = TreeNode(5)
    c = TreeNode(15)

    d = TreeNode(10)
    e = TreeNode(5)
    f = TreeNode(15)
    a.left = b
    a.right = c

    d.left = e
    e.right = f
    print Solution().isSameTree(a, d)
