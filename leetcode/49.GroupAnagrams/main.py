# coding=utf-8

class Solution(object):
    """
    给定一个字符串数组，将字母异位词组合在一起。字母异位词指字母相同，但排列不同的字符串。

    示例:

    输入: ["eat", "tea", "tan", "ate", "nat", "bat"],
    输出:
    [
    ["ate","eat","tea"],
    ["nat","tan"],
    ["bat"]
    ]
    说明：
    所有输入均为小写字母。
    不考虑答案输出的顺序。
    """
    char_dict = {
        "a": 2,
        "b": 3,
        "c": 5,
        "d": 7,
        "e": 11,
        "f": 13,
        "g": 17,
        "h": 19,
        "i": 23,
        "j": 29,
        "k": 31,
        "l": 37,
        "m": 41,
        "n": 43,
        "o": 47,
        "p": 53,
        "q": 59,
        "r": 61,
        "s": 67,
        "t": 71,
        "u": 73,
        "v": 79,
        "w": 83,
        "x": 89,
        "y": 97,
        "z": 101
    }

    def get_str_id3(self, s):
        """
        算s中每个字符出现的次数
        """
        r = [0] * 26
        for c in s:
            r[ord(c) - ord("a")] += 1
        return tuple(r)

    def get_str_id2(self, s):
        """
        算排序后的结果
        """
        return "".join(sorted(s))

    def get_str_id(self, s):
        r = 1
        for c in s:
            r *= self.char_dict[c]
        return r

    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        from collections import defaultdict
        d = defaultdict(lambda: [])
        for s in strs:
            s_id = self.get_str_id(s)
            d[s_id].append(s)

        return [v for k, v in d.iteritems()]


if __name__ == '__main__':
    print Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
