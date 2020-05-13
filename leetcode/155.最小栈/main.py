#!/usr/bin/env python
# coding=utf-8
import heapq

"""
设计一个支持 push ，pop ，top 操作，并能在常数时间内检索到最小元素的栈。

push(x) —— 将元素 x 推入栈中。
pop() —— 删除栈顶的元素。
top() —— 获取栈顶元素。
getMin() —— 检索栈中的最小元素。
 

示例:

输入：
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

输出：
[null,null,null,null,-3,null,0,-2]

解释：
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> 返回 -3.
minStack.pop();
minStack.top();      --> 返回 0.
minStack.getMin();   --> 返回 -2.

链接：https://leetcode-cn.com/problems/min-stack

解法1：利用最小堆
解法2：栈的特性是什么，后进先出，比如进栈顺序1，2，3，那么在3出站前，1，2不会出站，我们可以用这一点来将最小值放在一个辅助栈中。
辅助栈的元素代表该位置原始栈中该位置到栈底的最小值，每次压入元素前需要比较辅助栈顶和当前值，如果当前值更小则将当前值压入辅助栈。
否则仍将原值压入辅助栈。
"""


class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.st = []
        self.heap = []
        heapq.heapify(self.heap)

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.st.append(x)
        heapq.heappush(self.heap, x)

    def pop(self):
        """
        :rtype: None
        """
        x = self.st.pop()
        self.heap.remove(x)
        heapq.heapify(self.heap)

    def top(self):
        """
        :rtype: int
        """
        return self.st[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.heap[0]


class MinStack2(object):
    def __init__(self):
        self.stack = []
        self.min_stack = [float('inf')]

    def push(self, x):
        self.stack.append(x)
        self.min_stack.append(min(x, self.min_stack[-1]))

    def pop(self):
        self.stack.pop()
        self.min_stack.pop()

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.min_stack[-1]


if __name__ == '__main__':
    obj = MinStack()
    obj.push(-2)
    obj.push(0)
    obj.push(-1)
    print obj.getMin()
    print obj.top()
    obj.pop()
    print obj.getMin()
