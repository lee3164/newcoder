#include <iostream>
#include <vector>

using namespace std;

class Solution
{
public:
    int solution1(const vector<int> &array)
    {
        // 从前向后算，每次累加的结果和下一个比较，如果相加大于0，则继续比较
        // 如果小于0， 则结束，原因，当前的总和是m，下一个值是n，假设n后面的最大连续值是x
        // 则 m + n < 0 ，则 x + m + n < x，说明接下去继续比较肯定比x小，则不用比了

        int max = -100000;
        for (int i = 0; i < array.size(); ++i)
        {
            int t = array[i];
            if (t < 0) // 优化，如果当前值是个负数，那么肯定不是最大
            {
                if (t > max)
                    max = t;
                continue;
            }

            for (int j = i + 1; j < array.size(); ++j)
            {
                if (t + array[j] < 0)
                    break;
                t += array[j];
                if (t > max)
                    max = t;
            }
        }
        return max;
    }

    int solution2(const vector<int> &array)
    {
        // 动态规划，设 f(n) 为以a[n]结尾的最大子序列和
        // 则 f(n) = max { f(n-1)+a[n], a[n] }
        // 每次计算出来f值之后和之前最大的比较
        auto len = array.size();
        vector<int> f(len);
        f[0] = array[0];
        int max = f[0];
        for (int i = 1; i < len; ++i) {
            if (f[i-1] + array[i] < array[i]) {
                f[i] = array[i];
            } else {
                f[i] = f[i-1] + array[i];
            }
            if (f[i] > max)
                max = f[i];
        }
        return max;
    }

    int FindGreatestSumOfSubArray(vector<int> array)
    {
        return solution2(array);
    }
};

int main()
{
    cout << Solution().FindGreatestSumOfSubArray({1, -2, 3, 10, -4, 7, 2, -5}) << endl;
    return 0;
}