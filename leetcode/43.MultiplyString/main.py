# coding=utf-8

class Solution(object):
    """
    实现大数相乘，
    """
    def add(self, num1, num2):
        if len(num2) > len(num1):
            num1, num2 = num2, num1

        r = []
        b = 0
        for i, nums in enumerate(zip(reversed(num1), reversed(num2))):
            n1, n2 = nums
            s = int(n1) + int(n2) + b
            r.insert(0, str(s % 10))
            b = s / 10

        for i in num1[::-1][i+1:]:
            s = int(i) + b
            r.insert(0, str(s % 10))
            b = s / 10
        if b > 0:
            r.insert(0, str(b))

        return "".join(r)

    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1 == '0' or num2 == '0':
            return '0'
        r = "0"
        for i, n1 in enumerate(reversed(num1)):
            a = []
            b = 0
            for n2 in reversed(num2):
                m = int(n1) * int(n2) + b
                a.insert(0, str(m % 10))
                b = m / 10
            if b > 0:
                a.insert(0, str(b))
            a.extend(["0"] * i)
            r = self.add("".join(a), r)
        return r


if __name__ == '__main__':
    print Solution().add("1", "90")
