# coding=utf-8

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    """
    给定一个整数 n，生成所有由 1 ... n 为节点所组成的二叉搜索树。

示例:

输入: 3
输出:
[
  [1,null,3,2],
  [3,2,null,1],
  [3,1,null,null,2],
  [2,1,3],
  [1,null,2,null,3]
]
解释:
以上的输出对应以下 5 种不同结构的二叉搜索树：

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3

   
    """
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n == 0:
            return []
        used_nums = set()

        def build_tree(s, e, used_nums, dic):
            # type: (int, int, set[int], dict) -> list[TreeNode]
            if s > e:
                return [None]

            if (s, e) in dic:
                return dic[(s, e)]

            r = []
            i = s
            while i <= e:
                if i in used_nums:
                    i += 1
                    continue
                used_nums.add(i)

                lefts = build_tree(s, i - 1, used_nums, dic)
                rights = build_tree(i + 1, e, used_nums, dic)

                for left in lefts:
                    for right in rights:
                        root = TreeNode(i)
                        root.left = left
                        root.right = right
                        r.append(root)
                used_nums.remove(i)
                i += 1
            dic[(s, e)] = r
            return r

        return build_tree(1, n, used_nums, {})


if __name__ == '__main__':
    """
     1
    2 3
  4 5  6
    """
    print Solution().generateTrees(3)
