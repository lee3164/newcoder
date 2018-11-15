# coding=utf-8
import copy


class Solution(object):
    """
    给定 n 和 k，返回第 k 个排列。

    说明：
    给定 n 的范围是 [1, 9]。
    给定 k 的范围是[1,  n!]。
    
    示例 1:
    输入: n = 3, k = 3
    输出: "213"

    示例 2:
    输入: n = 4, k = 9
    输出: "2314"
    """
    def next_permutation(self, s):
        # 根据字符串得到其下一个排列
        i = len(s) - 1
        while i > 0 and s[i] < s[i - 1]:
            i -= 1
        j = i - 1
        k = i
        while j >= 0 and k + 1 < len(s) and s[k + 1] > s[j]:
            k += 1
        if j >= 0:
            s[k], s[j] = s[j], s[k]

        s[i:] = s[::-1][:len(s) - i]
        return s

    def getPermutation2(self, n, k):
        """
        传统方法一个个找，超时严重
        """
        # s = "".join(map(str, xrange(1, n + 1)))
        s = [str(i) for i in xrange(1, n + 1)]
        print s
        while k > 1:
            s = self.next_permutation(s)
            k -= 1

        return "".join(s)

    def getPermutation(self, n, k):
        """
        这个题目重在 找规律，比如输入 4，17，先来看4的全排列
        1234
        1243
        1324
        1342
        1423
        1432
        2134
        2143
        2314
        2341
        2413
        2431
        3124
        3142
        3214
        3241
        3412	<--- k = 17
        3421
        4123
        4132
        4213
        4231
        4312
        4321
        可以 看出，1，2，3，4这几个数字分别都出现了6次，也就是3！，这个很好理解，
        对于k来说，如果 1 <= k <= 6，第一个 肯定是1，7 <= k <= 12 ，肯定是2，依次类推，所以很好确定第一个数字
        此处第一个 数字是 17 / 6 + 1 = 3，是 1234中的第三个也就是3。
        那么接下来看k=17相当于 剩下的 1，2，4中第几个呢，由于在1234的全排列中第一个应该选3，故12开头的数字都出现了6次，也就是相当于在以3开头的
        数字中的第 17 - 6 * 2 = 5个，推广下，也就是 17 % 6 ==> 17 % 3!
        那么对于任意的n，k来说，选第一个数字 可以 根据 (n-1)!来计算，也就是第 i = k / (n-1)! + 1 个数字，那么对于 第i个前面的数字，每个都出现
        (n-1)!次，因此在剩下的数字中相当于 k % (n-1)!，我们重复这个过程，直到列表中没有数字可选即可
        """
        a = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
        b = [i for i in xrange(1, n + 1)]
        r = []
        while b:
            i = (k - 1) / a[n - 1]
            r.append(str(b[i]))
            b.remove(b[i])
            k = k % a[n - 1]
            n -= 1

        return "".join(r)


if __name__ == '__main__':
    print Solution().getPermutation(4, 9)
    # Solution().next_permutation([1,4,3,2])
