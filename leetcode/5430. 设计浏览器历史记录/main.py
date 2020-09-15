#!/usr/bin/env python
# coding=utf-8


class BrowserHistory(object):

    def __init__(self, homepage):
        """
        :type homepage: str
        """
        self.histories = [homepage]
        self.pos = 0

    def visit(self, url):
        """
        :type url: str
        :rtype: None
        """
        i = len(self.histories) - 1
        while i > self.pos:
            self.histories.pop()
            i -= 1

        self.histories.append(url)
        self.pos += 1

    def back(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        if self.pos - steps >= 0:
            self.pos -= steps
        else:
            self.pos = 0

        return self.histories[self.pos]

    def forward(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        if self.pos + steps < len(self.histories):
            self.pos += steps
        else:
            self.pos = len(self.histories) - 1

        return self.histories[self.pos]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
"""
["BrowserHistory","visit","visit","visit","back","back","forward","visit","forward","back","back"]
[["leetcode.com"],["google.com"],["facebook.com"],["youtube.com"],[1],[1],[1],["linkedin.com"],[2],[2],[7]]
"""

if __name__ == '__main__':
    b = BrowserHistory("leetcode.com")
    b.visit("google.com")
    b.visit("facebook.com")
    b.visit("youtube.com")
    print b.back(1)
    print b.back(1)
    print b.forward(1)
    b.visit("linkedin.com")
    print b.forward(2)
    print b.back(2)
    print b.back(7)
