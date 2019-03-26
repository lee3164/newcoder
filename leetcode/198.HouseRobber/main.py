# coding=utf-8
class Solution(object):
    """
    你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，
    影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。
    给定一个代表每个房屋存放金额的非负整数数组，计算你在不触动警报装置的情况下，能够偷窃到的最高金额。
    示例 1:

    输入: [1,2,3,1]
    输出: 4
    解释: 偷窃 1 号房屋 (金额 = 1) ，然后偷窃 3 号房屋 (金额 = 3)。
     偷窃到的最高金额 = 1 + 3 = 4 。
    示例 2:

    输入: [2,7,9,3,1]
    输出: 12
    解释: 偷窃 1 号房屋 (金额 = 2), 偷窃 3 号房屋 (金额 = 9)，接着偷窃 5 号房屋 (金额 = 1)。
     偷窃到的最高金额 = 2 + 9 + 1 = 12 。
    """
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        D = [0 for _ in nums]
        for index,num in enumerate(nums):
            if index == 0:
                D[index] = num
            elif index == 1:
                D[index] = max(D[index-1],num)
            else:
                D[index] = max(D[index-2]+num,D[index-1])
        return D[-1]

    def rob2(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if not nums:
        return 0
    a = {}
    b = {}
    for i, num in enumerate(nums):
        if i == 0:
            a[i] = num
            b[i] = 0;
        elif i == 1:
            a[i] = num
            b[i] = a[0]
        else:
            a[i] = b[i-1] + num
            b[i] = max(a[i-1], b[i-1])
            
    return max(a[i], b[i])