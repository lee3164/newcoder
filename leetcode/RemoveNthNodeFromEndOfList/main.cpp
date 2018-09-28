#include <iostream>

using namespace std;

/*
给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。
示例：
给定一个链表: 1->2->3->4->5, 和 n = 2.
当删除了倒数第二个节点后，链表变为 1->2->3->5.
说明：
给定的 n 保证是有效的。
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
    ListNode *removeNthFromEnd(ListNode *head, int n)
    {
        // 用一个节点先走n步，然后用一个节点开始同时走，p到终点的时候那么q恰好是倒数第n个
        ListNode *p = head, *q = head;
        ListNode *r = nullptr;
        for (int i = 0; i < n; ++i)
        {
            p = p->next;
        }
        while (p)
        {
            p = p->next;
            q = q->next;
            if (r)
            {
                r = r->next;
            }
            else
            {
                r = head;
            }
        }

        // 特殊case，r是nullptr的情况，也就是移除第一个链表的情况
        if (r)
            r->next = q->next;
        else
            head = head->next;
        return head;
    }
};

int main(int argc, char const *argv[]) { return 0; }
