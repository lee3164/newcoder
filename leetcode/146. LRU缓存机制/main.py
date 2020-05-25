#!/usr/bin/env python
# coding=utf-8

"""

运用你所掌握的数据结构，设计和实现一个  LRU (最近最少使用) 缓存机制。它应该支持以下操作： 获取数据 get 和 写入数据 put 。

获取数据 get(key) - 如果密钥 (key) 存在于缓存中，则获取密钥的值（总是正数），否则返回 -1。
写入数据 put(key, value) - 如果密钥已经存在，则变更其数据值；如果密钥不存在，则插入该组「密钥/数据值」。当缓存容量达到上限时，
它应该在写入新数据之前删除最久未使用的数据值，从而为新的数据值留出空间。



进阶:

你是否可以在 O(1) 时间复杂度内完成这两种操作？



示例:

LRUCache cache = new LRUCache( 2 /* 缓存容量 */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // 返回  1
cache.put(3, 3);    // 该操作会使得密钥 2 作废
cache.get(2);       // 返回 -1 (未找到)
cache.put(4, 4);    // 该操作会使得密钥 1 作废
cache.get(1);       // 返回 -1 (未找到)
cache.get(3);       // 返回  3
cache.get(4);       // 返回  4
"""


class ListNode(object):
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.last = None


class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.head = ListNode(0, 0)
        self.tail = ListNode(0, 0)
        self.node_dict = {}
        self.capacity = capacity
        self.size = 0

        self.head.next = self.tail
        self.tail.last = self.head

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.node_dict:
            return -1

        self.move_to_first(self.node_dict[key])
        return self.node_dict[key].val

    def delete_node(self, node):
        if node.last:
            node.last.next = node.next
        if node.next:
            node.next.last = node.last

    def move_to_first(self, node):
        self.delete_node(node)

        head = self.head
        head_next = self.head.next

        head.next = node
        node.last = head

        head_next.last = node
        node.next = head_next

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key not in self.node_dict:
            self.node_dict[key] = ListNode(key, value)
            self.size += 1

            if self.size > self.capacity:
                self.node_dict.pop(self.tail.last.key)
                self.delete_node(self.tail.last)
                self.size -= 1
        node = self.node_dict[key]
        node.val = value
        self.move_to_first(node)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


if __name__ == '__main__':
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    print cache.get(1)
    cache.put(3, 3)
    print cache.get(2)
    cache.put(4, 4)
    print cache.get(1)
    print cache.get(3)
    print cache.get(4)
