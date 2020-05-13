#!/usr/bin/env python
# coding=utf-8

"""
使用栈实现队列的下列操作：

push(x) -- 将一个元素放入队列的尾部。
pop() -- 从队列首部移除元素。
peek() -- 返回队列首部的元素。
empty() -- 返回队列是否为空。
示例:

MyQueue queue = new MyQueue();

queue.push(1);
queue.push(2);
queue.peek();  // 返回 1
queue.pop();   // 返回 1
queue.empty(); // 返回 false
说明:

你只能使用标准的栈操作 -- 也就是只有 push to top, peek/pop from top, size, 和 is empty 操作是合法的。
你所使用的语言也许不支持栈。你可以使用 list 或者 deque（双端队列）来模拟一个栈，只要是标准的栈操作即可。
假设所有操作都是有效的 （例如，一个空的队列不会调用 pop 或者 peek 操作）。

链接：https://leetcode-cn.com/problems/implement-queue-using-stacks


解法1：st1保存入栈顺序，st2保存出站顺序，栈先pop()出来压入另一个栈，可以实现先进先出
"""


class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.st1 = []
        self.st2 = []

    def _build(self):
        if self.st2:
            return
        while self.st1:
            self.st2.append(self.st1.pop())

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """
        self.st1.append(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        self.st2.pop()

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        return self.st2[-1]

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return len(self.st1) == 0 and len(self.st2) == 0
