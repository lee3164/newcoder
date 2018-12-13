# coding=utf-8


class Solution(object):
    """
    给定一个只包含数字的字符串，复原它并返回所有可能的 IP 地址格式。

    示例:

    输入: "25525511135"
    输出: ["255.255.11.135", "255.255.111.35"]

    1.长度0-3，2.大小0-255，3.00，000，01类似的不能算有效的，
    """
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        l = len(s)
        if l > 12 or l < 4:
            return []

        r = []

        def dfs(r, a, c, i):
            if c == 4:
                if i == l:
                    r.append(".".join(a))
                return

            for j in xrange(1, 4):
                if i + j > l:
                    return

                num = s[i:i + j]
                if 0 <= int(num) <= 255:
                    a.append(s[i:i + j])
                    dfs(r, a, c + 1, i + j)
                    a.pop()
                    if num == '0': # 如果当前的字符是0，不能和下一个结合，直接return即可
                        return

        dfs(r, [], 0, 0)

        return r


if __name__ == '__main__':
    print Solution().restoreIpAddresses("10001001")
