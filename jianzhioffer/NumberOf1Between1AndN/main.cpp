#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    int get_num_of_1(int n)
    {
        int num = 0;
        while (n > 0) {
            if (n % 10 == 1) {
                num += 1;
            }
            n /= 10;
        }
        return num;
    }

    int solution1(int n)
    {
        // 最蠢的做法，每个数字都算出来他们的1的个数
        int num = 0;
        while (n >= 1) {
            num += get_num_of_1(n--);
        }
        return num;
    }

    int solution2(int n)
    {
        vector<int> num_of_1_map(n+1);
        int num = 0;
        for (int i = 1; i <= n; ++i) {
            int j = i / 10;
            int j_num = num_of_1_map[j];
            int i_num = j_num;
            if (i % 10 == 1) {
                i_num = j_num + 1;
            }
            num += i_num;
            num_of_1_map[i] = i_num;
        }
        return num;
    }

    int solution3(int n) {
        int ones = 0;
        for (long long m = 1; m <= n; m *= 10)
            ones += (n/m + 8) / 10 * m + (n/m % 10 == 1) * (n%m + 1);
         return ones;
    }



    int NumberOf1Between1AndN_Solution(int n)
    {
        return solution2(n);
    }
};

int main()
{
    cout << Solution().NumberOf1Between1AndN_Solution(100000000) << endl;
    return 0;
}
