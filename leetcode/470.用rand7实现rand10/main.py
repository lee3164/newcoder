# coding=utf-8
import random


def rand7():
    return random.randint(1, 7)


class Solution(object):
    """
    主要在于思路，如何能够得到均匀分布的数字，
    枚举如下：
	a	1	2	3	4	5	6	7
b								
1		2	3	4	5	6	7	8
2		3	4	5	6	7	8	9
3		4	5	6	7	8	9	0
4		5	6	7	8	9	0	1
5		6	7	8	9	0	1	2
6		7	8	9	0	1	2	3
7		8	9	0	1	2	3	4
去掉右上角的  
6	7	8
7	8	9
8	9	0      后

每个数字的出现次数为4次，0-9的概率相同
    """

    def rand10(self):
        """
        :rtype: int
        """
        while True:
            a = rand7()
            b = rand7()
            if a <= 4 or b >= 4:
                return (a + b) % 10 + 1