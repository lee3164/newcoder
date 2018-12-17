# coding=utf-8

class Solution(object):
    """
    给定三个字符串 s1, s2, s3, 验证 s3 是否是由 s1 和 s2 交错组成的。

    示例 1:

    输入: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
    输出: true
    示例 2:

    输入: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
    输出: false

    中间很多重复计算的子集，需要记忆，不记得话会超时
    """
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        l1 = len(s1)
        l2 = len(s2)
        l3 = len(s3)
        if l1 + l2 != l3:
            return False

        def helper(i, p, q, dic):
            if i == l3:
                return i == p + q

            if (i, p, q) in dic:
                return dic[(i, p, q)]

            # 如果都在长度范围内且3者相等，无法确定用哪一个，此时应该两个都应该试试，
            # 如果有确定的 如2，3的判断条件，直接下一步

            if p < l1 and q < l2 and s1[p] == s2[q] == s3[i]:
                r = helper(i + 1, p + 1, q, dic) or helper(i + 1, p, q + 1, dic)
            elif p < l1 and s1[p] == s3[i]:
                r = helper(i + 1, p + 1, q, dic)
            elif q < l2 and s2[q] == s3[i]:
                r = helper(i + 1, p, q + 1, dic)
            else:
                r = False
            dic[(i, p, q)] = r
            return r

        return helper(0, 0, 0, {})


if __name__ == '__main__':
    print Solution().isInterleave("aabcc", "dbbca", "aadbbcbcac")
