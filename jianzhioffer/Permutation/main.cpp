/*
输入一个字符串,按字典序打印出该字符串中字符的所有排列。例如输入字符串abc,
则打印出由字符a,b,c所能排列出来的所有字符串abc,acb,bac,bca,cab和cba。
输入一个字符串,长度不超过9(可能有字符重复),字符只包括大小写字母。
*/

#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

class Solution {
public:
    void PermutationImpl(string &str, int start, vector<string>& res) {
        int len = str.size();
        if (start == len - 1)
        {
            auto s = str;  // here str is the right ordered seq; so push it into vector
            res.push_back(s);
        }

        bool exist[127] { false };
//        for (int i = 0; i < 127; ++i)
//        {
//            exist[i] = false;
//        }

        // swap to the start, no need copy;  use postion to replace
        for (int i = start; i < len; ++i)
        {
            if (exist[str[i]])
                continue;
            exist[str[i]] = true;
            swap(str[i], str[start]);
            PermutationImpl(str, start+1, res);
            swap(str[i], str[start]);
        }
    }

    vector<string> Permutation(string str) {
        vector<string> res;
        PermutationImpl(str, 0, res);
        sort(res.begin(), res.end()); // sort at last, no need sort in the impl
        return res;
    }
};


int main()
{
    auto ret = Solution().Permutation("abcd");
    for (auto s :ret) {
        cout << s << endl;
    }
    return 0;
}
