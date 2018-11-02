# coding=utf-8

class Solution(object):
    """
    给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
    上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。 感谢 Marcos 贡献此图。

    示例:
    输入: [0,1,0,2,1,0,1,3,2,1,2,1]
    输出: 6

    双指针法，一个指向头，一个指向尾，根据短板定理，从小的开始算，比如开始 l小一些，那么从l开始向r遍历，如果l+1比r小，增加 相应体积，如此反复
    """
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        v = 0
        l, r = 0, len(height) - 1
        while l < r:
            if height[l] < height[r]:
                i = l + 1
                while i < r and height[i] < height[l]:
                    v += (height[l] - height[i])
                    i += 1
                l = i
            else:
                i = r - 1
                while i > l and height[i] < height[r]:
                    v += (height[r] - height[i])
                    i -= 1
                r = i
        return v

    def trap2(self, heights):
        pass


if __name__ == '__main__':
    print Solution().trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])
