#!/usr/bin/env python
# coding=utf-8

"""
给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。

求在该柱状图中，能够勾勒出来的矩形的最大面积。
以上是柱状图的示例，其中每个柱子的宽度为 1，给定的高度为 [2,1,5,6,2,3]。
图中阴影部分为所能勾勒出的最大矩形面积，其面积为 10 个单位。
 
示例:

输入: [2,1,5,6,2,3]
输出: 10

链接：https://leetcode-cn.com/problems/largest-rectangle-in-histogram

s[i, j] = min(h[i]~h[j]) * j-i+1
"""
import copy


class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        l = []
        r = 0
        for i, h in enumerate(heights):
            while l and l[-1] > h:
                l.pop()
            l.append(h)

            j = 0
            l2 = copy.copy(l)
            while j <= i:
                r = max((i - j + 1) * l2[0], r)
                if heights[j] == l2[0]:
                    l2.pop(0)
                j += 1
        return r

    def largestRectangleArea2(self, heights):
        """
        高度固定的情况下，i,j同时像两边延展，当遇见第一个小于当前高度的时候，i，j停止，
        此时的 面积是  s = h * (i-j-1)
        如果每个位置都需要两边延展找i，j，最坏情况需要遍历整个数组，复杂度是N2
        如果我们能预先算出左侧和右侧，小于当前位置高度的位置i，j，那么在遍历的时候
        可以直接算最大面积。

        单调栈：值得是站内元素是单调的，我们用来存储高度，
        高度循环进栈，如果栈顶高度大于等于当前h，那么依次出站，直到栈为空或者栈顶元素小于当前h
        此时我们就得到了在该位置之前比第一个当前h小的最小高度的位置, 如果栈为空，那么就存-1
        -1这个位置代表无穷小，遍历一遍即可计算出所有位置中左边第一个比当前h小的位置
        同理求右边
        """
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
    print Solution().largestRectangleArea2([2, 1, 5, 6, 2, 3])
