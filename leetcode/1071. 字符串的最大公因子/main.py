#!/usr/bin/env python
# coding=utf-8

class Solution(object):

    def getMin(self, s):
        i = 1
        while i <= len(s) / 2:
            if len(s) % i != 0:
                continue

            t = s[:i]
            j = i
            while j < len(s):
                if t != s[j:j + i]:
                    break
                j += i
            else:
                return t

            i += 1
        return s

    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        minLen = min(len(str1), len(str2))
        for i in xrange(minLen):
            if str1[i] != str2[i]:
                return ""

        s1 = self.getMin(str1)
        s2 = self.getMin(str2)

        if s1 != s2:
            return ""

        m = len(str1) / len(s1)
        n = len(str2) / len(s2)

        def gcd(a, b):
            if a % b == 0:
                return b
            else:
                return gcd(b, a % b)

        return gcd(m, n) * s1


if __name__ == '__main__':
    print Solution().gcdOfStrings("abc", "abcabc")
