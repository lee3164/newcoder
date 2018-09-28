#include <iostream>

using namespace std;

/*
将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 
示例：
输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4
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
    ListNode *mergeTwoLists(ListNode *l1, ListNode *l2)
    {
        // 归并排序的思想
        ListNode *q = nullptr;
        ListNode dummy(0); 
        ListNode *p = &dummy; // 此处弄一个虚拟节点很有用，避免写很多判断代码
        while (l1 && l2)
        {
            if (l1->val < l2->val)
            {
                q = l1;
                l1 = l1->next;
            }
            else
            {
                q = l2;
                l2 = l2->next;
            }
            p->next = q;
            p = p->next;
        }
        if (l1)
            p->next = l1;
        if (l2)
            p->next = l2;
        return dummy.next;
    }
};

int main()
{
    return 0;
}
