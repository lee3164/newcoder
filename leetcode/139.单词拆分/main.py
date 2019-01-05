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
    给定一个非空字符串 s 和一个包含非空单词列表的字典 wordDict，判定 s 是否可以被空格拆分为一个或多个在字典中出现的单词。

说明：

拆分时可以重复使用字典中的单词。
你可以假设字典中没有重复的单词。
示例 1：

输入: s = "leetcode", wordDict = ["leet", "code"]
输出: true
解释: 返回 true 因为 "leetcode" 可以被拆分成 "leet code"。
示例 2：

输入: s = "applepenapple", wordDict = ["apple", "pen"]
输出: true
解释: 返回 true 因为 "applepenapple" 可以被拆分成 "apple pen apple"。
     注意你可以重复使用字典中的单词。
示例 3：

输入: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
输出: false

两种思路，dfs和dp，dfs会超时，能否用字典树减枝？
    """
    def wordBreak2(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """

        def dfs(b, e):
            if e == len(s):
                return b == e

            for i in xrange(e, len(s)):
                if s[b:i + 1] in wordDict and dfs(i + 1, i + 1):
                    return True
            return False

        return dfs(0, 0)

    def wordBreak(self, s, wordDict):
        wordDict = set(wordDict)
        f = [True for _ in xrange(len(s) + 1)]
        for i in xrange(1, len(s) + 1):
            f[i] = False
            for j in xrange(0, i):
                if f[j] and s[j:i] in wordDict:
                    f[i] = True

        return f[-1]


if __name__ == '__main__':
    print Solution().wordBreak(s="applepenapple", wordDict=["apple", "pen"])
