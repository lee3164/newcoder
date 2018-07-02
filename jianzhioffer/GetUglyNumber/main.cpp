#include <iostream>
#include <vector>

using namespace std;

/*
 * 把只包含因子2、3和5的数称作丑数（Ugly Number）。
 * 例如6、8都是丑数，但14不是，因为它包含因子7。 习惯上我们把1当做是第一个丑数。求按从小到大的顺序的第N个丑数。
 * */

class Solution {
public:
    int solution1(int index) {
        // 丑数定义 f = 2^x * 3^y * 5^z
        // 思路：任何一个丑数都是由前面的某一个丑数乘以2，3，5得到的，只不过*2，*3，*5跨度不同，增长有快慢。
        // 因此记录每次x，y，z已经变化的值，每次尝试将x，y，z分别+1，选最小的，例如*2是最小的，x+1，如果有相同的，都加1
        vector<int> arr{1};
        int x = 0, y = 0, z = 0;
        for (int i = 1; i < index; ++i) {
            int m = min(arr[x] * 2, min(arr[y] * 3, arr[z] * 5));
            arr.push_back(m);
            if (m == arr[x] * 2) ++x;
            if (m == arr[y] * 3) ++y;
            if (m == arr[z] * 5) ++z;
        }
        return arr[index-1];
    }

    int GetUglyNumber_Solution(int index) {
        return solution1(index);
    }
};

int main()
{
    cout << Solution().GetUglyNumber_Solution(100) << endl;
    return 0;
}