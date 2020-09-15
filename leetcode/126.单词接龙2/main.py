# coding=utf-8
from collections import defaultdict
from copy import copy
import string


class Solution(object):
    """
    给定两个单词（beginWord 和 endWord）和一个字典 wordList，找出所有从 beginWord 到 endWord 的最短转换序列。转换需遵循如下规则：

    每次转换只能改变一个字母。
    转换过程中的中间单词必须是字典中的单词。
    说明:

    如果不存在这样的转换序列，返回一个空列表。
    所有单词具有相同的长度。
    所有单词只由小写字母组成。
    字典中不存在重复的单词。
    你可以假设 beginWord 和 endWord 是非空的，且二者不相同。
    示例 1:

    输入:
    beginWord = "hit",
    endWord = "cog",
    wordList = ["hot","dot","dog","lot","log","cog"]

    输出:
    [
    ["hit","hot","dot","dog","cog"],
    ["hit","hot","lot","log","cog"]
    ]
    示例 2:

    输入:
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot","dot","dog","lot","log"]

    输出: []

    解释: endWord "cog" 不在字典中，所以不存在符合要求的转换序列。
    """

    def buildGraph1(self, wordList):
        m = defaultdict(set)
        i = 0
        while i < len(wordList) - 1:
            j = i + 1
            while j < len(wordList):
                wi, wj = wordList[i], wordList[j]
                flag = False
                for ci, cj in zip(wi, wj):
                    if ci != cj:
                        if not flag:
                            flag = True
                        else:
                            flag = False
                            break
                if flag:
                    m[wi].add(wj)
                    m[wj].add(wi)
                j += 1
            i += 1
        return m

    def buildGraph2(self, wordList):
        m = defaultdict(set)
        wordList = set(wordList)
        for word in wordList:
            c_list = list(word)
            i = 0
            while i < len(c_list):
                origin_c = c_list[i]
                for c in string.lowercase:
                    if c == origin_c:
                        continue
                    c_list[i] = c
                    w = "".join(c_list)
                    if w in wordList:
                        m[word].add(w)
                        m[w].add(word)
                c_list[i] = origin_c
                i += 1
        return m

    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: list[str]
        :rtype: list[list[str]]
        """
        if endWord not in wordList:
            return []
        wordList.append(beginWord)
        if len(wordList) <= 57:
            m = self.buildGraph1(wordList)
        else:
            m = self.buildGraph2(wordList)

        # 利用bfs快速检验是否能到达和深度，避免盲目dfs
        def bfs(q, visited):
            level_dict = {}
            level = 1
            while q:
                level += 1
                new_q = []
                for w in q:
                    for w2 in m[w]:
                        if w2 in visited:
                            continue
                        new_q.append(w2)
                        visited.add(w2)
                        level_dict[w2] = level
                q = new_q
            return level_dict

        level_dict = bfs([beginWord], {beginWord})
        level_dict[beginWord] = 1

        if not endWord in level_dict:
            return []

        def dfs(word, l, r, s):
            if len(l) > level_dict[word]:
                return
            if word == endWord:
                r.append(copy(l))
                return
            for w in m[word]:
                if w in l:
                    continue
                l.append(w)
                dfs(w, l, r, s)
                l.pop()

        r = []
        dfs(beginWord, [beginWord], r, set())

        return r

    def findLadders2(self, beginWord, endWord, wordList):
        if endWord not in wordList:
            return []

        m = defaultdict(set)
        wordList = set(wordList)
        wordList.add(beginWord)
        for w1 in wordList:
            for w2 in wordList:
                if w1 == w2:
                    continue
                d = 0
                for c1, c2 in zip(w1, w2):
                    if c1 != c2:
                        d += 1
                    if d > 1:
                        break
                if d == 1:
                    m[w1].add(w2)
                    m[w2].add(w1)

        r = []
        q = [[beginWord]]
        visited = set()
        need_break = False
        while q:
            new_q = []
            for wl in q:
                w1 = wl[-1]

                for w2 in m[w1]:
                    if w2 in visited:
                        continue

                    t = copy(wl)
                    t.append(w2)
                    if w2 != endWord:
                        new_q.append(t)
                    else:
                        r.append(t)
                        need_break = True

                visited.add(w1)

            q = new_q
            if need_break:
                break

        return r

    def findLadders3(self, beginWord, endWord, wordList):
        if endWord not in wordList:
            return []

        m = defaultdict(set)
        wordList = set(wordList)
        wordList.add(beginWord)
        for w1 in wordList:
            for w2 in wordList:
                if w1 == w2:
                    continue
                d = 0
                for c1, c2 in zip(w1, w2):
                    if c1 != c2:
                        d += 1
                    if d > 1:
                        break
                if d == 1:
                    m[w1].add(w2)
                    m[w2].add(w1)

        r = []
        begin = {beginWord}
        end = {endWord}

        visited = set()
        forward = True
        paths = defaultdict(list)
        paths[beginWord] = [[beginWord]]
        paths[endWord] = [[endWord]]
        need_break = False
        while begin and end:
            if len(begin) > len(end):
                begin, end = end, begin
                forward = not forward

            tmp = set()
            for w1 in begin:
                for w2 in m[w1]:
                    if w2 in visited:
                        continue

                    if w2 in paths:
                        for p1 in paths[w1]:
                            for p2 in paths[w2]:
                                if forward:
                                    r.append(p1 + p2)
                                else:
                                    r.append(p2 + p1)
                        need_break = True
                    else:
                        for p in paths[w1]:
                            t = copy(p)
                            if forward:
                                t.append(w2)
                            else:
                                t.insert(0, w2)
                            paths[w2].append(t)

                    tmp.add(w2)
                visited.add(w1)

            begin = tmp
            if need_break:
                break
        return r


if __name__ == '__main__':
    wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
    print Solution().findLadders3("hit", "cog", wordList)
