//题目描述
//输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。要求不能创建任何新的结点，只能调整树中结点指针的指向。

#include <iostream>

using namespace std;

struct TreeNode
{
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
    TreeNode(int x) :
            val(x), left(NULL), right(NULL)
    {
    }
};

class Solution {
public:

    TreeNode* Convert(TreeNode* pRootOfTree)
    {
        if (!pRootOfTree)
            return pRootOfTree;
        TreeNode* pre = nullptr;
        ConvertImpl(pRootOfTree, pre);
        TreeNode* left = pRootOfTree;
        while (left && left->left)
            left = left->left;
        return left;
    }

    /*
        pre存的是上一轮之后 链表最右边的节点
    */

    TreeNode* ConvertImpl(TreeNode* cur, TreeNode* &pre)
    {
        if (!cur)
            return cur;
        ConvertImpl(cur->left, pre);
        cur->left = pre;
        if (pre)
            pre->right = cur;
        pre = cur;
        ConvertImpl(cur->right, pre);
    }
};


int main()
{
    cout << "Hello World!" << endl;
    return 0;
}
