#include <iostream>
#include <vector>
#include <map>

using namespace std;

/*
数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。例如输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}。
由于数字2在数组中出现了5次，超过数组长度的一半，因此输出2。如果不存在则输出0。
*/

class Solution {
public:
    int solution1(const vector<int>& numbers) {
        // 最简单的一种写法，遍历数组，算当前数字出现次数，并且比对当前出现次数是否超过了一半的大小
        auto len = numbers.size();
        map<int, int> count;
        for (auto& num: numbers) {
            if (count.find(num) != count.cend()) {
                count[num] += 1;
            } else {
                count[num] = 1;
            }
            if (count[num] > len / 2)
            {
                return num;
            }
        }
        return 0;
    }

    int solution2(const vector<int>& numbers) {
        // 打“擂台”的方式，不同两个数字同时消失，相同的则次数加1，当count==0的时候，
        // 说明上次的两个数字已经抵消了，
        // 最后留下的数字不一定是出现次数最多的，所以要验证，如1,2,2,1,3，最后则会留下3
        int count = 0, val;
        for (auto& num: numbers) {
            if (count == 0){
                val = num;
                count++;
            } else if (val == num) {
                count++;
            } else {
                count--;
            }
        }
        count = 0;
        for (auto& num: numbers) {
            if (val == num) {
                count++;
            }
        }
        if (count > numbers.size() / 2)
            return val;
        return 0;
    }

    int MoreThanHalfNum_Solution(vector<int> numbers) {
        return solution2(numbers);
    }
};

int main()
{
    Solution solution;
    cout << solution.MoreThanHalfNum_Solution({1,2,3,2,2,2,5,4,2});
    return 0;
}
