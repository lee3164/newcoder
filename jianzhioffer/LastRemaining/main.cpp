#include <iostream>
#include <queue>
#include <vector>
#include <list>

using namespace std;
Sum_Soluti
//http://zhedahht.blog.163.com/blog/static/2541117420072250322938/

class Solution {
public:
    int solution1(int m, int n)
    {
        queue<int> p, q;
        for (int i = 0; i < n; ++i)
            p.push(i);

        int count = 0;
        while (p.size() != 1)
        {
            while (p.size() != 0)
            {
                if (count == m - 1)
                {
                    p.pop();
                    count = 0;
                    continue;
                }
                int n = p.front();
                q.push(n);
                p.pop();
                ++count;
            }
            swap(p, q);
        }
        return p.front();
    }

    int solution2(int n, int m)
    {
            list<int> arr;
            for (int i = 0; i < n; ++i)
                arr.push_back(i);

            auto it = arr.begin();
            while (arr.size() != 1)
            {
                for (int i = 0; i < m - 1; ++i)
                {
                    ++it;
                    if (it == arr.end())
                        it = arr.begin();
                }
                it = arr.erase(it);
                if (it == arr.end())
                    it = arr.begin();
            }
            return arr.front();
    }

    int LastRemaining_Solution(int n, int m)
    {
        return solution2(n, m);
    }
};

int main()
{
    cout << Solution().LastRemaining_Solution(4, 5) << endl;
    return 0;
}
