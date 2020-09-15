#!/usr/bin/env python
# coding=utf-8

class Solution(object):
    def dailyTemperatures(self, T):
        """
        从右至左的单调栈，栈内元素从底到顶递减
        每次遇见一个新元素将比自己小的元素pop出来，
        这样就知道了右边第一个比自己大的，然后自己入栈
        """
        st = []
        r = [0 for _ in T]
        i = len(T) - 1
        while i >= 0:
            while st and T[st[-1]] <= T[i]:
                st.pop()

            if st:
                r[i] = st[-1] - i

            st.append(i)
            i -= 1

        return r

    def dailyTemperatures2(self, T):
        """
        从左到右的单调栈，如果当前元素比左边的大，说明肯定是第一个大的
        因为如果之前有比栈里面的元素大的，早就出栈了
        """
        st = []
        r = [0 for _ in T]
        for i, t in enumerate(T):

            while st and T[st[-1]] < t:
                prev = st.pop()
                r[prev] = i - prev

            st.append(i)

        return r
