# coding=utf-8


class Solution(object):
    """
    一条包含字母 A-Z 的消息通过以下方式进行了编码：

    'A' -> 1
    'B' -> 2
    ...
    'Z' -> 26
    给定一个只包含数字的非空字符串，请计算解码方法的总数。

    示例 1:

    输入: "12"
    输出: 2
    解释: 它可以解码为 "AB"（1 2）或者 "L"（12）。
    示例 2:

    输入: "226"
    输出: 3
    解释: 它可以解码为 "BZ" (2 26), "VF" (22 6), 或者 "BBF" (2 2 6) 。

    如果当前数字可以独立存在，则f[i] = f[i-1]，除了0之外，
    如果当前数字还可以和上一个合起来，则f[i] += f[i-2]，边界条件比较多，主要是
    和0相关的，比如0不能独立存在，前一个如果是0的话也不能合并起来
    """
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int

        12 => 2
        12 3 =>
        """
        if s[0] == '0':
            return 0

        f = {-1: 1, 0: 1}

        i = 1
        while i < len(s):
            if s[i] == '0' and s[i - 1] != '1' and s[i - 1] != '2':
                return 0

            if s[i - 1] == '1' or (s[i - 1] == '2' and '0' <= s[i] <= '6'):
                if s[i] == '0':
                    f[i] = f[i - 2]
                else:
                    f[i] = f[i - 1] + f[i - 2]
            else:
                f[i] = f[i - 1]

            i += 1

        return f[i - 1]

    def numDecodings2(self, s):
        """
        更加简洁的写法
        """
        if s[0] == '0':
            return 0
        dp = [0] * (len(s) + 1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2, len(s) + 1):
            if s[i - 1] > '0':
                dp[i] = dp[i - 1]
            if s[i - 2] == '1' or (s[i - 2] == '2' and s[i - 1] <= '6'):
                dp[i] += dp[i - 2]
        return dp[len(s)]


if __name__ == '__main__':
    print Solution().numDecodings("230")
