#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/8 上午9:16
# @Email   : lixiaoyu@bytedance.com
from __future__ import absolute_import, unicode_literals


def lengthOfLongestSubstring(s):
    char_set = set()
    longest_len = 0
    i = j = 0
    while i < len(s) and j < len(s):
        if s[i] not in char_set:
            longest_len = max(longest_len, i - j + 1)
            char_set.add(s[i])
            i += 1
        else:
            char_set.remove(s[j])
            j += 1

    return longest_len


if __name__ == '__main__':
    print lengthOfLongestSubstring("abba")
