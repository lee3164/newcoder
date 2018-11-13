# coding=utf-8

class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    def __repr__(self):
        return "[{}, {}]".format(self.start, self.end)


class Solution(object):
    """
    给出一个区间的集合，请合并所有重叠的区间。

    示例 1:

    输入: [[1,3],[2,6],[8,10],[15,18]]
    输出: [[1,6],[8,10],[15,18]]
    解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
    示例 2:

    输入: [[1,4],[4,5]]
    输出: [[1,5]]
    解释: 区间 [1,4] 和 [4,5] 可被视为重叠区间。
    """
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if not intervals:
            return []

        # 使用 sorted 比 sort慢很多
        # intervals = sorted(intervals, key=lambda val: val.start)
        intervals.sort(key=lambda val: val.start)

        interval = intervals[0]
        i = 1
        r = []

        # 每次合并下一个，如果不能合并，加入返回
        while i < len(intervals):
            if interval.end >= intervals[i].start:
                interval = Interval(interval.start, max(intervals[i].end, interval.end))
            else:
                r.append(interval)
                interval = intervals[i]
            i += 1

        # 最后合并完了肯定没有 append进来，这里append下
        if interval:
            r.append(interval)
        return r


if __name__ == '__main__':
    print Solution().merge([
        Interval(1, 4),
        Interval(2, 3),
    ])
