#include <iostream>
#include <vector>

using namespace std;

//统计一个数字在排序数组中出现的次数。

class Solution
{
public:
    int find(vector<int> &data, int start, int end, int k)
    {
        // 二分查找的方式
        if (start == end)
        {
            if (data[start] == k)
                return 1;
            return 0;
        }
        if (start == end - 1)
        {
            int count = 0;
            if (data[start] == k)
                count += 1;
            if (data[end] == k)
                count += 1;
            return count;
        }
        int mid = start + (end - start) / 2; // mid = (start + end) / 2   ->    start <= mid < end
        if (data[mid] > k)
        {
            return find(data, start, mid - 1, k);
        }
        else if (data[mid] < k)
        {
            return find(data, mid + 1, end, k);   // 此处可以直接mid+1
        }
        else
        {
            return 1 + find(data, start, mid - 1, k) + find(data, mid + 1, end, k);
        }
    }

    int solution1(vector<int> &data, int k)
    {
        return find(data, 0, data.size() - 1, k);
    }

    int get_first_k(vector<int> &data, int k)
    {
        int s = 0, e = data.size() - 1;
        while (s <= e)
        {
            int m = (s + e) / 2;
            if (data[m] < k)
            {
                s = m + 1;
            }
            else if (data[m] > k)
            {
                e = m - 1;
            }
            else
            {
                if (s == m && data[s] == data[m])
                    return s;
                else
                    e = m - 1;
            }
        }
        return -1;
    }

    int get_last_k(vector<int> &data, int k)
    {
        int s = 0, e = data.size() - 1;
        while (s <= e)
        {
            int m = (s + e) / 2;
            if (data[m] < k)
            {
                s = m + 1;
            }
            else if (data[m] > k)
            {
                e = m - 1;
            }
            else
            {
                if (e == m && data[e] == data[m])
                    return s;
                else
                    s = m + 1;
            }
        }
        return -1;
    }

    int solution2(vector<int> &data, int k)
    {
        int s = get_first_k(data, k);
        int e = get_last_k(data, k);

        if (s == -1)
            return 0;

        return e - s + 1;
    }


    int GetNumberOfK(vector<int> data, int k)
    {
        return solution2(data, k);
    }
};

int main()
{
    cout << Solution().GetNumberOfK({1,2,3,3,3,3,4,5}, 3) << endl;
    return 0;
}