class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []


class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


def generate_tree(nums):
    if not nums:
        return None
    nodes = []
    for num in nums:
        if num is None:
            nodes.append(None)
        else:
            nodes.append(TreeNode(num))

    p_idx = 0
    c_idx = 1
    while c_idx < len(nodes):
        if nodes[p_idx]:
            nodes[p_idx].left, nodes[p_idx].right = nodes[c_idx:c_idx + 2]
        p_idx += 1
        c_idx += 2

    return nodes[0]


from collections import defaultdict
from copy import copy
import string


class Solution(object):
    """
    给定一个非空字符串 s 和一个包含非空单词列表的字典 wordDict，在字符串中增加空格来构建一个句子，使得句子中所有的单词都在词典中。返回所有这些可能的句子。

说明：

分隔时可以重复使用字典中的单词。
你可以假设字典中没有重复的单词。
示例 1：

输入:
s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
输出:
[
  "cats and dog",
  "cat sand dog"
]
示例 2：

输入:
s = "pineapplepenapple"
wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
输出:
[
  "pine apple pen apple",
  "pineapple pen apple",
  "pine applepen apple"
]
解释: 注意你可以重复使用字典中的单词。
示例 3：

输入:
s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]
输出:
[]
    """
    def wordBreak(self, s, wordDict):
        wordDict = set(wordDict)
        f = [True for _ in xrange(len(s) + 1)]
        d = defaultdict(list)
        for i in xrange(1, len(s) + 1):
            f[i] = False
            for j in xrange(0, i):
                if f[j] and s[j:i] in wordDict:
                    f[i] = True
                    d[j].append(i)

        if not f[-1]:
            return []

        r = []

        def dfs(b, r, l):
            if b == len(s):
                r.append(copy(l))
                return
            for e in d[b]:
                l.append(s[b:e])
                dfs(e, r, l)
                l.pop()

        dfs(0, r, [])
        return [" ".join(i) for i in r]


if __name__ == '__main__':
    print Solution().wordBreak(s="pineapplepenapple",
                               wordDict=["apple", "pen", "applepen", "pine", "pineapple"])
