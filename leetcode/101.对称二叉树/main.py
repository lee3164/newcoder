# coding=utf-8

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    """
    给定一个二叉树，检查它是否是镜像对称的。
    错误做法：用中序遍历，然后判断是不是镜像对称，如果是对称的，中序遍历也是对称，但是反过来不一定，如下：
         1
      2    3
    3   N 2  N
    这个中序遍历也是32123，但是不是镜像对称

    正确解法：1.层次遍历，判断每层是否镜像对称；
            2.递归，具体看代码，容易理解
    """
    def isSymmetric(self, root):
        if not root:
            return True
        queue = [root.left, root.right]
        while queue:
            i, j = 0, len(queue) - 1
            while i < j:
                if (not queue[i] and queue[j] or not queue[j] and queue[i]) or \
                        (queue[i] and queue[j] and queue[i].val != queue[j].val):
                    return False
                i += 1
                j -= 1

            new_queue = []
            for node in queue:
                if node:
                    new_queue.append(node.left)
                    new_queue.append(node.right)
            queue = new_queue
        return True

    def isSymmetric2(self, root):
        if not root:
            return True

        def helper(left, right):
            if (not left and right or not right and left) or \
                    (left and right and left.val != right.val):
                return False
            elif not left and not right:
                return True
            else:
                return helper(left.left, right.right) and helper(left.right, right.left)

        return helper(root.left, root.right)

    def isSymmetricWrong(self, root):
        if not root:
            return True

        l = []
        st = []
        while root or st:
            if not root:
                root = st.pop()
                l.append(root.val)
                root = root.right
            else:
                st.append(root)
                root = root.left

        if len(l) % 2 == 0:
            return False

        i = 0
        j = len(l) - 1
        while i < j:
            if l[i] != l[j]:
                return False
            i += 1
            j -= 1

        return True


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
    print Solution().isSymmetric(a)
