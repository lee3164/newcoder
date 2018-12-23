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
    给定一个非负整数 numRows，生成杨辉三角的前 numRows 行。
    在杨辉三角中，每个数是它左上方和右上方的数的和。

示例:

输入: 5
输出:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
    """
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        r = []
        for i in xrange(numRows):
            l = []
            for j in xrange(i + 1):
                if j == 0 or j == i:
                    l.append(1)
                else:
                    l.append(r[i - 1][j - 1] + r[i - 1][j])
            r.append(l)

        return r


if __name__ == '__main__':
    print Solution().generate(5)
