#include <iostream>
#include <vector>
#include <algorithm>
#include <numeric>
#include <functional>

using namespace std;

/*
一个整型数组里除了两个数字之外，其他的数字都出现了偶数次。请写程序找出这两个只出现一次的数字。
*/
/*
（1）第一次使用异或运算，得到了两个只出现一次的数相异或的结果。
（2）因为两个只出现一次的数肯定不同，即他们的异或结果一定不为0，一定有一个位上有1。另外一个此位上没有1，
    我们可以根据此位上是否有1，将整个数组重新划分成两部分，一部分此位上一定有1，另一部分此位上一定没有1，
    然后分别对每部分求异或，因为划分后的两部分有这样的特点：其他数都出现两次，只有一个数只出现一次。
    因此，我们又可以运用异或运算，分别得到两部分只出现一次的数。
*/
class Solution
{
public:
    void FindNumsAppearOnce(vector<int> data,int* num1,int *num2)
    {
        int res = accumulate(data.begin(), data.end(), 0, bit_xor<int>());
        int i = 0;
        int j = 1;
        while (true) {
            j = 1 << i;
            if (j & res)
                break;
            ++i;
        }
        *num1 = 0;
        *num2 = 0;
        for (auto i=0; i < data.size(); ++i)
        {
            if (data[i] & j)
                *num1 ^= data[i];
            else
                *num2 ^= data[i];
        }
    }
};
int main()
{
    int num1, num2;
    Solution().FindNumsAppearOnce({1,2,3,1,2,3,4,5,4, 5, 1, 1, 8, 9}, &num1, &num2);
    cout << num1 << " " << num2 << endl;
    return 0;
}
