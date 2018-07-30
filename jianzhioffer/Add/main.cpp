#include <iostream>

using namespace std;
//写一个函数，求两个整数之和，要求在函数体内不得使用+、-、*、/四则运算符号。
/*
（以下分析来自剑指offer）比如我们计算5+17=22这个结果，世界上，我们可以分为3个步骤计算，第一步各位数相加不进位，
此时的结果是12（个位相加不进位是2，十位相加是1），所以结果是12； 第二步做进位，5+7有进位，进位值是10；
第三步是把前两步计算结果加起来。12 + 10 = 22.

那么运用位运算二进制的数字也可以这么考虑，5是二进制的101,17是二进制的10001。试着把计算分为3步走，第一步各位相加不进位，得到的结果是10100；第二步是记下进位，根据这个例子进位计算结果是10；第三步是把前两步计算结果相加得到结果10110.转化为10进制刚好是22。 用二进制计算，第一步不考虑进位，即每一位相加 0+0=0,1+1=0,0+1=1,1+0=1。结果符合二进制数据的异或运算。第二步只考虑进位运算，0+0,0+1,1+0都不会进位，只有1+1才会进位，结果符合两个数的与运算结果然后向左移动一位。第三步，把前两步骤的结果相加，相加步骤仍然是重复前两步骤。直到不产生进位值。

*/
class Solution {
public:
    int solution1(int num1, int num2)
    {
        int i, j;
        do {
            i = (num1 & num2) << 1;
            j = (num1 ^ num2);
            num1 = i;
            num2 = j;
        }while(num1 != 0);
        return num2;
    }

    int solution2(int num1, int num2)
    {
        char* p = reinterpret_cast<char*>(num1);
        return reinterpret_cast<long>(&(p[num2])); // here must be long, because of percision
    }

    int Add(int num1, int num2)
    {
        return solution2(num1, num2);
    }
};

int main()
{
    cout << Solution().Add(210000000, 10) << endl;
    return 0;
}
