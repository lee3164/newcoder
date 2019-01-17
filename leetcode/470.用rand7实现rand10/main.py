import random


def rand7():
    return random.randint(1, 7)


class Solution(object):
    def rand10(self):
        """
        :rtype: int
        """
        while True:
            a = rand7()
            b = rand7()
            if a <= 4 or b >= 4:
                return (a + b) % 10 + 1