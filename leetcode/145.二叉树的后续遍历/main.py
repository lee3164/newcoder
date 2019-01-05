class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []


class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


def generate_tree(nums):
    if not nums:
        return None
    nodes = []
    for num in nums:
        if num is None:
            nodes.append(None)
        else:
            nodes.append(TreeNode(num))

    p_idx = 0
    c_idx = 1
    while c_idx < len(nodes):
        if nodes[p_idx]:
            nodes[p_idx].left, nodes[p_idx].right = nodes[c_idx:c_idx + 2]
        p_idx += 1
        c_idx += 2

    return nodes[0]


from collections import defaultdict
from copy import copy
import string


class Solution(object):
    def postorderTraversal(self, root):
        """
        所有节点都入栈，入栈顺序是 根，右，左，出栈的时候注意当pre是cur的子节点的时候，
        说明之前已经访问子节点了，当前节点可以出栈，否则的话还需要将其子节点入栈
        """
        if not root:
            return []

        r = []
        st = [root]
        pre = cur = None
        while st:
            cur = st[-1]
            if (not cur.left and not cur.right) or (pre and (pre == cur.left or pre == cur.right)):
                r.append(cur.val)
                st.pop()
                pre = cur
            else:
                if cur.right: st.append(cur.right)
                if cur.left: st.append(cur.left)

        return r

    def postorderTraversal2(self, root):
        """
        后序遍历是左右根，
        如果我们求出 根右左，然后反过来就行
        根右左类似与前序遍历
        """
        if not root:
            return []
        r = []
        st = [root]
        while st:
            cur = st.pop()
            r.append(cur.val)
            if cur.left: st.append(cur.left)
            if cur.right: st.append(cur.right)

        return r[::-1]

if __name__ == '__main__':
    a = generate_tree([1, 2, 3, 4, 5, 6, 7])
    print Solution().postorderTraversal2(a)
