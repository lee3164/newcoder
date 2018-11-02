# coding=utf-8


class Solution(object):
    """
    报数序列是一个整数序列，按照其中的整数的顺序进行报数，得到下一个数。其前五项如下：

    1.     1
    2.     11
    3.     21
    4.     1211
    5.     111221
    1 被读作  "one 1"  ("一个一") , 即 11。
    11 被读作 "two 1s" ("两个一"）, 即 21。
    21 被读作 "one 2",  "one 1" （"一个二" ,  "一个一") , 即 1211。
    给定一个正整数 n（1 ≤ n ≤ 30），输出报数序列的第 n 项。
    注意：整数顺序将表示为一个字符串。
    示例 1:
    输入: 1
    输出: "1"

    示例 2:
    输入: 4
    输出: "1211"

    下一个排列由上一个得出，递归最简单，非递归也不难
    """

    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return "1"
        arr = []
        s = self.countAndSay(n - 1)
        i = 0
        while i < len(s):
            j = i + 1
            while j < len(s) and s[i] == s[j]:
                j += 1
                continue
            arr.append(str(j - i))
            arr.append(s[i])
            i = j
        return "".join(arr)

    def countAndSay2(self, n):
        s = "1"
        for i in range(0, n - 1):
            arr = []
            i = 0
            while i < len(s):
                j = i + 1
                while j < len(s) and s[i] == s[j]:
                    j += 1
                    continue
                arr.append(str(j - i))
                arr.append(s[i])
                i = j
            s = "".join(arr)
        return s


if __name__ == '__main__':
    print Solution().countAndSay2(4)
