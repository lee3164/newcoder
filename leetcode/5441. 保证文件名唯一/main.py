#!/usr/bin/env python
# coding=utf-8

class Solution(object):
    def getFolderNames(self, names):
        """
        :type names: List[str]
        :rtype: List[str]
        """
        r = []
        d = {}
        for name in names:
            i = len(name) - 1
            bs = -1
            be = -1
            num = 0
            base = 1
            while i >= 0:
                c = name[i]
                if bs == -1 and c == "(":
                    bs = i
                    break
                elif be == -1 and c == ")":
                    be = i
                elif be > -1 and '0' <= c <= '9':
                    num = num + base * int(c)
                    base *= 10
                elif be > -1:
                    break
                i -= 1

            if num != 0:
                prefix = name[0:bs]
                d.setdefault(prefix, set())
                d[prefix].add(num)

            if name in d:
                i = 0
                while i in d[name]:
                    i += 1
                if i > 0:
                    new_name = "{}({})".format(name, i)
                    r.append(new_name)
                    d.setdefault(new_name, set())
                    d[new_name].add(0)
                else:
                    r.append(name)
                d[name].add(i)
            else:
                d.setdefault(name, set()),
                d[name].add(0)
                r.append(name)

        return r


if __name__ == '__main__':
    print Solution().getFolderNames(
        ["r", "y", "m", "o(3)(2)", "f", "r", "z", "u", "w", "q(2)(3)", "a", "s", "k", "o", "y", "b", "n", "t(2)(4)",
         "s", "e", "r", "v", "g", "q(1)(4)", "j", "j", "r(4)(4)", "t"])
