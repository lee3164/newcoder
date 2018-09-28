#include <iostream>

using namespace std;

/*
给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。
示例:
给定 1->2->3->4, 你应该返回 2->1->4->3.
说明:
你的算法只能使用常数的额外空间。
你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
*/

struct ListNode
{
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

class Solution
{
  public:
    ListNode *func(ListNode *head)
    {
        // 首先排除特殊情况，即null和只有一个节点
        if (!head || !head->next)
            return head;

        // 此时确定有两个节点，j肯定要指向i，而i到底指向哪一个依赖后面的反转情况
        // 因此继续递归

        ListNode* i = head;
        ListNode* j = i->next;
        ListNode* k = j->next;
        j->next = i;
        i->next = func(k);
        return j;
    }
    ListNode *solution1(ListNode *head)
    {
        // 递归解决，
        return func(head);
    }

    ListNode *swapPairs(ListNode *head)
    {
        return solution1(head);
    }
};

int main()
{
    return 0;
}