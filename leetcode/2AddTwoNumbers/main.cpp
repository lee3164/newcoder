#include <iostream>

/*
给定两个非空链表来表示两个非负整数。位数按照逆序方式存储，它们的每个节点只存储单个数字。将两数相加返回一个新的链表。
你可以假设除了数字 0 之外，这两个数字都不会以零开头。

示例：
输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807
 * /

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
struct ListNode
{
    int val;
    ListNode *next;
    ListNode(int x)
        : val(x), next(NULL)
    {}
};

class Solution
{
public:
    ListNode *solution1(ListNode *l1, ListNode *l2)
    {
        // 有点小啰嗦，不够简洁，符合常人思维，先处理 两个链表都不为空，在处理一个链表不为空，最后处理都为空的时候的进位
        int extra = 0;
        ListNode *node = new ListNode(-1);
        ListNode *head = node;
        while (l1 && l2)
        {
            int res = l1->val + l2->val + extra;
            int val;
            if (res >= 10)
            {
                val = res - 10;
                extra = 1;
            }
            else
            {
                val = res;
                extra = 0;
            }
            if (node->val == -1)
            {
                node->val = val;
            }
            else
            {
                node->next = new ListNode(val);
                node = node->next;
            }
            l1 = l1->next;
            l2 = l2->next;
        }
        ListNode *remain_list = nullptr;
        if (l1)
            remain_list = l1;
        else
            remain_list = l2;
        while (remain_list)
        {
            int res = remain_list->val + extra;
            int val;
            if (res >= 10)
            {
                val = res - 10;
                extra = 1;
            }
            else
            {
                val = res;
                extra = 0;
            }
            node->next = new ListNode(val);
            node = node->next;
            remain_list = remain_list->next;
        }
        if (extra)
            node->next = new ListNode(extra);
        return head;
    }

    ListNode *addTwoNumbers(ListNode *l1, ListNode *l2)
    {
        // 比较简洁的写法，每次运算生成下一次的节点，并且将进位加进去
        ListNode *node = new ListNode(0);
        ListNode *head = node;
        while (l1 || l2)
        {
            if (l1) node->val += l1->val, l1 = l1->next;
            if (l2) node->val += l2->val, l2 = l2->next;
            if (l1 || l2 || node->val >= 10) // 此处判断逻辑是 l1，l2是否有下一位，或者有进位，满足条件需要提前生成下一位的节点
            {
                int val = 0;
                if (node->val >= 10)
                {
                    node->val -= 10;
                    val = 1;
                }
                node->next = new ListNode(val);
                node = node->next;
            }
        }
        return head;
    }
};

int main()
{
    ListNode * a = new ListNode(2);
    a->next = new ListNode(4);
    a->next->next = new ListNode(3);

    ListNode* b = new ListNode(5);
    b->next = new ListNode(6);
    b->next->next = new ListNode(4);

    Solution().addTwoNumbers(a, b);

    return 0;
}