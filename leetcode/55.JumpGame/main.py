# coding=utf-8

class Solution(object):
    """
    给定一个非负整数数组，你最初位于数组的第一个位置。
    数组中的每个元素代表你在该位置可以跳跃的最大长度。
    判断你是否能够到达最后一个位置。

    示例 1:
    输入: [2,3,1,1,4]
    输出: true
    解释: 从位置 0 到 1 跳 1 步, 然后跳 3 步到达最后一个位置。

    示例 2:
    输入: [3,2,1,0,4]
    输出: false
    解释: 无论怎样，你总会到达索引为 3 的位置。但该位置的最大跳跃长度是 0 ， 所以你永远不可能到达最后一个位置。
    """
    def canJump(self, nums):
        """
        这个比较简单，根据当前位置算出上一个能到这里的位置，然后递归
        """

        def func(idx):
            if idx == 0:
                return True
            for i in xrange(1, idx + 1):
                if nums[idx - i] >= i:
                    # 这里为啥可以直接return，如果idx-i到不了idx这个位置，就不用继续向前看了吗？
                    # 如果 idx-i可以到达该位置，idx-j也可以到达 idx位置（j > i），
                    # 那么idx - j 肯定可以到达idx-i的位置，所以算idx-i 和 算 idx-j没区别，
                    # 可以直接return
                    return func(idx - i) 

            return False

        return func(len(nums) - 1)

    def canJump2(self, nums):
        """
        这里的意思是 算出前面的数字能够到达的最远值，
        """

        maxreach = 0
        for i, num in enumerate(nums):
            if i > maxreach:   # 因为i>maxreach，说明前面的到达 当前位置，没有继续比较的需要了
                return False

            # 能到达这里的，说明至少maxreach >= i 
            maxreach = max(maxreach, num + i)  # 算出当前可以到达的最远
            if maxreach >= len(nums) - 1:
                return True


if __name__ == '__main__':
    print Solution().canJump([5, 0, 2, 0, 4])
