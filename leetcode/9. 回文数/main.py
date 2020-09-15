#!/usr/bin/env python
# coding=utf-8

class Solution(object):
    def isPalindrome(self, x):
        """
        如果是回文数，倒过来也是一样的
        """
        if x < 0:
            return False

        t = x
        y = 0
        while t > 0:
            y = y * 10 + t % 10
            t /= 10

        return x == y

    def isPalindrome2(self, x):
        """
        不需要全部倒过来，到一半即可，如1221， 12 21 倒过来一半就能个判断了
        如果是 12321这样的，需要 12， 3， 21 这样判断
        """
        # 下面的判断无法判断10这样的，因此先排除掉
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        y = 0
        while x > y:
            y = y * 10 + x % 10
            x /= 10

        return x == y or x == y / 10


if __name__ == '__main__':
    print Solution().isPalindrome2(10)
