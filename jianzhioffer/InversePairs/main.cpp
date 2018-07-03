#include <iostream>
#include <vector>

using namespace std;

/*
* 在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。
* 输入一个数组,求出这个数组中的逆序对的总数P。并将P对1000000007取模的结果输出。
* 即输出P%1000000007
*/

class Solution {
public:
    int solution1(const vector<int>& arr) {
        int count = 0;
        for (int i = 0; i < arr.size(); ++i)
            for (int j = i + 1; j < arr.size(); ++j) {
                if (arr[i] > arr[j])
                    ++count;
            }
        return count % 1000000007;
    }

    /*
        归并排序的思想，如果对于两个排好序的数组，当前面数组的数大于后面的数组的数的时候，
        则逆序对是后面的数组的当前位置到起始位置的总个数
        如 [6,7,8,9], [1,2,3,4] 最开始的时候 i=>9 j=>4, 此时9>4，那么产生了9和前面的任意一个都组成逆序对
        --i，类似进行比较，如果arr[i] < arr[j]，则--j
    */

    void sort(vector<int>& arr, int start, int mid, int end, unsigned long& count) {
        vector<int> sorted_arr;
        int i = mid, j = end;
        while (i >= start && j >= mid+1) {
            if (arr[i] > arr[j]) {
                sorted_arr.push_back(arr[i--]);
                count += (j - mid);
            }
            else
                sorted_arr.push_back(arr[j--]);
        }
        while (i >= start)
            sorted_arr.push_back(arr[i--]);
        while (j >= mid+1)
            sorted_arr.push_back(arr[j--]);
        int k = end;
        for (int i = 0; i < sorted_arr.size(); ++i)
            arr[k--] = sorted_arr[i];
    }

    void split(vector<int> &arr, int start, int end, unsigned long& count) {
        if (end == start)
            return;
        int mid = start + (end - start) / 2;
        split(arr, start, mid, count);
        split(arr, mid+1, end, count);
        sort(arr, start, mid, end, count);
    }

    int solution2(vector<int> &arr) {
        unsigned long count = 0;
        split(arr, 0, arr.size()-1, count);
        return count % 1000000007;
    }

    int InversePairs(vector<int> data) {
        return solution2(data);
    }
};

int main()
{
    cout << Solution().InversePairs({1,2,3,4,5,6,7,0}) << endl;
    return 0;
}
