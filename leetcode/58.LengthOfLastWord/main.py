# coding=utf-8

class Solution(object):
    """
    求最后一个单词的长度
    """
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = 0
        s = s.rstrip()
        if not s:
            return 0
        for c in reversed(s):
            if ord('A') <= ord(c) <= ord('z'):
                l += 1
            else:
                break

        return l


if __name__ == '__main__':
    print Solution().lengthOfLastWord(" cCGiKdpcAjnbQbewGXqQDKuuwcg")
