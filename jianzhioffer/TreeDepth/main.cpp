#include <iostream>
#include <queue>

using namespace std;

/*
 * 输入一棵二叉树，求该树的深度。从根结点到叶结点依次经过的结点（含根、叶结点）形成树的一条路径，
 * 最长路径的长度为树的深度。
 * */

struct TreeNode
{
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
    TreeNode(int x)
        :
        val(x), left(NULL), right(NULL)
    {
    }
};

class Solution
{
public:
    int solution1(TreeNode* root)
    {
        // 递归写法，统计左子树和右子树的长度，然后比较
        if (!root)
            return 0;
        int left = solution1(root->left);
        int right = solution1(root->right);
        return std::max(left, right) + 1;
    }

    int solution2(TreeNode* root)
    {
        if (!root)
            return 0;
        queue<TreeNode*> nodes;
        nodes.push(root);
        int depth = 0;

        // 一层层处理，每次处理一层节点，处理前算出size，即本层需要处理的数量，
        // 然后一个个弹出，加入下一层的节点，算高度
        while (!nodes.empty())
        {
            ++depth;
            auto size = nodes.size();
            for (decltype(size) i = 0; i < size; ++i)
            {
                auto node = nodes.front();
                nodes.pop();
                if (node->left)
                    nodes.push(node->left);
                if (node->right)
                    nodes.push(node->right);
            }
        }
        return depth;
    }

    int TreeDepth(TreeNode *pRoot)
    {
        return solution1(pRoot);
    }
};

int main()
{
    std::cout << "Hello, World!" << std::endl;
    return 0;
}