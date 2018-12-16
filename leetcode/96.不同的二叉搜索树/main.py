# coding=utf-8

class Solution(object):
    """
    给定一个整数 n，求以 1 ... n 为节点组成的二叉搜索树有多少种？

示例:

输入: 3
输出: 5
解释:
给定 n = 3, 一共有 5 种不同结构的二叉搜索树:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3

   f[n] = f[0]*f[n-1] + f[1]*f[n-2] + ... + f[n-1]*f[0]
    """
    def numTrees(self, n):
        if n == 0:
            return 0

        def build_tree(s, e, dic):
            dis = e - s + 1
            if dis == 0:
                return 1
            if dis in dic:
                return dic[dis]

            count = 0
            for i in xrange(s, e + 1):
                left = build_tree(s, i - 1, dic)
                right = build_tree(i + 1, e, dic)
                count += left * right

            dic[dis] = count
            return count

        return build_tree(1, n, {})

    def numTrees2(self, n):
        dp = [0] * (n + 1)
        dp[0] = 1
        for i in range(1, n + 1):
            for j in range(i):
                dp[i] += dp[j] * dp[i - j - 1]
        return dp[-1]


if __name__ == '__main__':
    """
     1
    2 3
  4 5  6
    """
    print Solution().numTrees2(10)
