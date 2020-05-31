#!/usr/bin/env python
# coding=utf-8


"""
给定一个仅包含 0 和 1 的二维二进制矩阵，找出只包含 1 的最大矩形，并返回其面积。

示例:

输入:
[
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]
输出: 6

链接：https://leetcode-cn.com/problems/maximal-rectangle
"""


class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        x = len(matrix)
        y = len(matrix[0])

        i = 0
        s = 0
        heights = [0 for _ in xrange(y)]
        while i < x:
            j = 0
            while j < y:
                k = i
                h = 0
                while k < x and matrix[k][j] == '1':
                    h += 1
                    k += 1

                heights[j] = h
                j += 1
            s = max(s, self.maxS(heights))
            i += 1

        return s

    def maxS(self, heights):
        left = [-1 for _ in heights]
        right = [len(heights) for _ in heights]

        st = []
        i = 0
        while i < len(heights):
            while st and heights[st[-1]] >= heights[i]:
                st.pop()

            if st:
                left[i] = st[-1]

            st.append(i)
            i += 1

        st = []
        i = len(heights) - 1
        while i >= 0:
            while st and heights[st[-1]] >= heights[i]:
                st.pop()

            if st:
                right[i] = st[-1]

            st.append(i)
            i -= 1

        s = 0
        for i, h in enumerate(heights):
            s = max(s, h * (right[i] - left[i] - 1))

        return s


if __name__ == '__main__':
    matrix = [
        ["0", "1"],
        ["1", "0"],
    ]
    print Solution().maximalRectangle(matrix)
