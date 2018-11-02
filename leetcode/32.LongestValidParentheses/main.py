# coding=utf-8


class Solution(object):
    """
    给定一个只包含 '(' 和 ')' 的字符串，找出最长的包含有效括号的子串的长度。
    示例 1:
    输入: "(()"
    输出: 2
    解释: 最长有效括号子串为 "()"
    示例 2:
    输入: ")()())"
    输出: 4
    解释: 最长有效括号子串为 "()()"
    实例 3：
    输入："()(()"
    输出： 2

    思路：是找合法子串的最大长度，注意实例3这样的。大致括号有两种情况，一种是嵌套的，即(xxxx)，xxxx里面也是各种合法的嵌套，
    还有(xxx)(xxx)类似这样的，这种会增加子串长度，我们使用栈来记录有效括号，用一个dict记录当前)的前一个有效最长的(，
    如f[3] = 2，则代表，第2个和第3个分别是()，此外还可以进行合并，如果f[3] = 2 ，而f[1] = 0，则说明括号排列是()()，这样的
    所以f[3] = f[1] = 0，依次从左往右，因为左边的是明确可以确定的匹配，所有往右的时候不断合并，并算出最大长度
    """

    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        pairs = {}
        count = 0
        for i, c in enumerate(s):
            if c == '(':
                stack.append(i)
            elif len(stack) != 0:
                if stack[-1] - 1 in pairs:
                    pairs[i] = pairs[stack[-1] - 1]
                else:
                    pairs[i] = stack[-1]
                count = max(count, i - pairs[i] + 1)
                stack.pop()

        return count


if __name__ == '__main__':
    print Solution().longestValidParentheses('(()()()')
