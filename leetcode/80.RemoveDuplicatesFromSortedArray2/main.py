# coding=utf-8
class Solution(object):
    def removeDuplicates(self, nums):
        """
        给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素最多出现两次，
        返回移除后数组的新长度。 不要使用额外的数组空间，
        你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。

        示例 1:
        给定 nums = [1,1,1,2,2,3],
        函数应返回新长度 length = 5, 并且原数组的前五个元素被修改为 1, 1, 2, 2, 3 。
        你不需要考虑数组中超出新长度后面的元素。
        
        示例 2:
        给定 nums = [0,0,1,1,1,1,2,3,3],
        函数应返回新长度 length = 7, 并且原数组的前五个元素被修改为 0, 0, 1, 1, 2, 3, 3 。
        你不需要考虑数组中超出新长度后面的元素。
        """
        if not nums:
            return 0

        s = 1
        count = 1

        i = 1
        while i < len(nums):
            if nums[i] == nums[i - 1]:
                count += 1
            else:
                count = 1

            # 最开始 是这样写的，此处是交换位置，如1，1，1，2，2，2
            # 变成 这样的时候1，1，2，2，1，2，此时上面的逻辑会根据前面和后面是否相等来判断是否重复
            # 这里最后一个2本来应该判断重复的，但是由于把1换过来了，导致判断不成功，2和1会再换一次
            # 导致问题，而当用下面的只赋值的做法，不会破坏后面的数组性质，因此是对的
            # if count <= 2:
            #     if i != s:
            #         nums[s], nums[i] = nums[i], nums[s]
            #     s += 1

            if count <= 2:
                nums[s] = nums[i]
                s += 1

            i += 1

        return s

     def removeDuplicates2(self, nums):
        """
        超赞的做法，前两个肯定是不会有问题的，后面的可以直接根据 
        当前项和前面两项比较，不同的话移到前面去
        注意，此处位于i之前的数字是已经符合题意的数字，i是下一个要写入的位置
        如果 e == nums[i-2]说明e在nums已经有了两个，应该跳过这个，否则说明
        e不满足，可以写入
        """
        i = 0
        for e in nums:
            if i < 2 or e != nums[i - 2]:
                nums[i] = e
                i += 1

        return i


if __name__ == '__main__':
    print Solution().removeDuplicates([1, 1, 1, 2, 2, 2, 3, 3])
