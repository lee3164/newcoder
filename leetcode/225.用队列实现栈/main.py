#!/usr/bin/env python
# coding=utf-8

"""
使用队列实现栈的下列操作：

push(x) -- 元素 x 入栈
pop() -- 移除栈顶元素
top() -- 获取栈顶元素
empty() -- 返回栈是否为空
注意:

你只能使用队列的基本操作-- 也就是 push to back, peek/pop from front, size, 和 is empty 这些操作是合法的。
你所使用的语言也许不支持队列。 你可以使用 list 或者 deque（双端队列）来模拟一个队列 , 只要是标准的队列操作即可。
你可以假设所有操作都是有效的（例如, 对一个空的栈不会调用 pop 或者 top 操作）。

1. 用两个队列实现，push直接加入list1，pop和top先将前n-1个存到另外一个队列，弹出后交换；push o(1) pop&top o(n)
2. 用一个队列，push的时候将前n-1个一次弹出然后append到尾部，使得最新的元素始终在第一个位置，push o(n) pop&top o(1)

"""


class MyStack(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.l1 = []
        self.l2 = []

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: None
        """
        self.l1.append(x)

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        while len(self.l1) > 1:
            self.l2.append(self.l1.pop(0))

        self.l1, self.l2 = self.l2, self.l1
        return self.l2.pop(0)

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        while len(self.l1) > 1:
            self.l2.append(self.l1.pop(0))
        return self.l1[0]

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return len(self.l1) == 0 and len(self.l2) == 0


class MyStack2(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.l = []

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: None
        """
        self.l.append(x)
        i = 0
        while i < len(self.l) - 1:
            i += 1
            self.l.append(self.l.pop(0))

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        return self.l.pop(0)

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        return self.l[0]

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return len(self.l) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()

if __name__ == '__main__':
    obj = MyStack()
    obj.push(1)
    obj.push(2)
    obj.push(3)
    print obj.top()
