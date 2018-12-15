# coding=utf-8

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        st = []
        r = []
        left_flag = True
        while True:
            if root.left and left_flag:
                st.append(root)
                root = root.left
                continue

            left_flag = True
            r.append(root.val)
            if root.right:
                root = root.right
            elif st:
                root = st.pop()
                left_flag = False
            else:
                break
        return r

    def inorderTraversal2(self, root):
        r = []
        st = []

        c = root
        while c or st:
            if c:
                st.append(c)
                c = c.left
            else:
                p = st[-1]
                st.pop()
                r.append(p.val)
                c = p.right

        return r


if __name__ == '__main__':
    """
     1
    2 3
  4 5  6
    """
    a = TreeNode(1)
    b = TreeNode(2)
    c = TreeNode(3)
    d = TreeNode(4)
    e = TreeNode(5)
    f = TreeNode(6)
    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f
    print Solution().inorderTraversal2(a)
