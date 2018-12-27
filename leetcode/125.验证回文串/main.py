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


class Solution(object):
    def is_valid_char(self, c):
        return '0' <= c <= '9' or 'A' <= c <= 'Z'

    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.upper()
        i, j = 0, len(s) - 1
        while i < j:
            while i < len(s) and not self.is_valid_char(s[i]):
                i += 1
            while j >= 0 and not self.is_valid_char(s[j]):
                j -= 1
            if i < j and s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True


if __name__ == '__main__':
    print Solution().isPalindrome("`l;`` 1o1 ??;l`")
