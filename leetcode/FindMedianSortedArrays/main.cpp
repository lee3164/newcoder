#include <iostream>
#include <vector>

using namespace std;

/*
给定两个大小为 m 和 n 的有序数组 nums1 和 nums2 。
请找出这两个有序数组的中位数。要求算法的时间复杂度为 O(log (m+n)) 。
你可以假设 nums1 和 nums2 均不为空。
*/

class Solution
{
public:
    double findMedianSortedArrays(const vector<int> &nums1, const vector<int> &nums2)
    {
        auto size1 = nums1.size(), size2 = nums2.size();
        int target = (size1 + size2 + 1) / 2;
        bool need_two_num = false;
        if ((size1 + size2) % 2 == 0)
            need_two_num = true;

        int a = 0, b = 0;
        int p = 0, q = 0;
        for (int i = 0; i < target; ++i)
        {
            if (nums1[p] < nums1[q])
                a = nums1[p++];
            else
                a = nums2[q++];
        }

        if (need_two_num)
        {
            if (nums1[p] < nums1[q])
                b = nums1[p];
            else
                b = nums2[q];
        }

        return (static_cast<double>(a) + static_cast<double>(b)) / 2;
    }
};

void print_vector(const vector<int> &vec)
{
    for (const auto &num: vec)
    {
        cout << num << endl;
    }
}

int main()
{
    vector<int> a{1, 2};
    vector<int> b{3};
    print_vector(a);
    print_vector(b);
    std::cout << Solution().findMedianSortedArrays(a, b) << std::endl;
    return 0;
}