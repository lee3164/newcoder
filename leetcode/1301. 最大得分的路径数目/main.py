#!/usr/bin/env python
# coding=utf-8

class Solution(object):
    def pathsWithMaxScore(self, board):
        """
        :type board: List[str]
        :rtype: List[int]
        """
        m = len(board)
        n = len(board[0])

        f = [[0 for _ in xrange(n)] for _ in xrange(m)]
        d = [[0 for _ in xrange(n)] for _ in xrange(m)]

        i = m - 1
        while i >= 0:
            j = n - 1
            while j >= 0:
                if board[i][j] == 'S':
                    f[i][j] = 0
                    d[i][j] = 1
                elif board[i][j] == 'X':
                    f[i][j] = float("-inf")
                else:
                    c = board[i][j]
                    s = 0
                    if '0' <= c <= '9':
                        s = int(c)

                    if i == m - 1:
                        f[i][j] = s + f[i][j + 1]
                        d[i][j] = d[i][j + 1]
                    elif j == n - 1:
                        f[i][j] = s + f[i + 1][j]
                        d[i][j] = d[i + 1][j]
                    else:
                        max_f = max(f[i][j + 1], f[i + 1][j], f[i + 1][j + 1])
                        f[i][j] = max_f + s
                        if f[i][j + 1] == max_f:
                            d[i][j] += d[i][j + 1]
                        if f[i + 1][j] == max_f:
                            d[i][j] += d[i + 1][j]
                        if f[i + 1][j + 1] == max_f:
                            d[i][j] += d[i + 1][j + 1]

                j -= 1
            i -= 1

        if f[0][0] < 0:
            return 0, 0

        return f[0][0], d[0][0]


if __name__ == '__main__':
    b = ["E11345", "X452XX", "3X43X4", "422812", "284522", "13422S"]

    print Solution().pathsWithMaxScore(b)
