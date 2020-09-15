#!/usr/bin/env python
# coding=utf-8

"""
给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。

示例 1:

输入: s = "anagram", t = "nagaram"
输出: true
示例 2:

输入: s = "rat", t = "car"
输出: false
说明:
你可以假设字符串只包含小写字母。

链接：https://leetcode-cn.com/problems/valid-anagram
"""

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        d = {}
        for c in s:
            d.setdefault(c, 0)
            d[c] += 1

        for c in t:
            if c not in d:
                return False
            d[c] -= 1

        for c, cnt in d.items():
            if cnt != 0:
                return False

        return True