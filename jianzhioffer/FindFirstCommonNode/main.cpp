#include <iostream>
#include <set>
#include <vector>
#include <stack>

using namespace std;

// 寻找两个链表的公共节点
// 如果有公共节点，那么呈Y字形

struct ListNode
{
    int val;
    struct ListNode *next;
    ListNode(int x)
        :
        val(x), next(NULL)
    {
    }
};

class Solution
{
public:
    ListNode *solution1(ListNode *pHead1, ListNode *pHead2)
    {
        // 插入其中一个的节点到set中，然后进行比较
        set<ListNode *> nodes;
        ListNode *node = pHead1;
        while (node != nullptr)
        {
            nodes.insert(node);
            node = node->next;
        }
        node = pHead2;
        while (node != nullptr)
        {
            if (nodes.count(node) == 1)
                return node;
            node = node->next;
        }
        return nullptr;
    }

    ListNode *solution2(ListNode *pHead1, ListNode *pHead2)
    {
        // 利用从尾部节点比较，从后数最后一个也就是从前往后的第一个公共节点
        stack<ListNode *> stack1, stack2;
        ListNode *i = pHead1, *j = pHead2;
        while (i != nullptr)
        {
            stack1.push(i);
            i = i->next;
        }
        while (j != nullptr)
        {
            stack2.push(j);
            j = j->next;
        }

        // 一定是Y字形，如果栈顶的都不相同，那么一定都没有相同的节点
        if (stack1.top() != stack2.top())
            return nullptr;

        // 如果有，则进行下面的步骤
        ListNode *common_node = nullptr;
        while (!stack1.empty() && !stack2.empty())
        {
            if (stack1.top() == stack2.top())
            {
                common_node = stack1.top();
                stack1.pop();
                stack2.pop();
            }
            // 如果栈顶不等了的时候，马上结束就行
            return common_node;
        }
    }

    ListNode *solution3(ListNode *pHead1, ListNode *pHead2)
    {
        // 先走A再走B，或先走B再走A，最终都能到达统一目的地，如果有公共节点，并且是同时到达，因为走的总步数一样
        // 所以相遇的地方一定是第一个公共节点，这样才可能一起走到终点
        ListNode *p = pHead1, *q = pHead2;
        int count = 0;
        while (p != q)
        {
            if (p) p = p->next;
            if (q) q = q->next;

            // 注意此处可能可能没有公共节点，无论是AB顺序还是BA顺序，到最后都会走一样的步数，
            // 也就是说p,q最后都会等于nullptr，所以一定会退出循环
            // 这里的这个逻辑是 p走完了A之后换B走的和q走完B之后换A走的逻辑
            if (p != q)
            {
                if (!p) p = pHead2;
                if (!q) q = pHead1;
            }
        }
        return p;
    }

    ListNode *FindFirstCommonNode(ListNode *pHead1, ListNode *pHead2)
    {

    }
};

int main()
{
    std::cout << "Hello, World!" << std::endl;
    return 0;
}