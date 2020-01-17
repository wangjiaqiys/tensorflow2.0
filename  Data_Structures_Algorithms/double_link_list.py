# _*_ coding:utf-8 _*_
"""
双向链表
前驱节点 prev/prior
后继节点 next
"""
import
class Node():
    """双向链表节点"""
    def __init__(self, item):
        self.item = item
        self.next = None
        self.prev = None

class DoubleLinkList():
    def __init__(self, node=None):
        self.__head = node
    def is_empty(self):
        """判断链表是否为空"""
        return self.__head is None
    def length(self):
        """返回链表的长度"""
        cur = self.__head
        count = 0
        while cur != None:
            count += 1
            cur = cur.next
        return count
    def travle(self):
        """遍历链表"""
        cur = self.__head
        while cur != None:
            print(cur.item, end=" ")
            cur = cur.next
    def add(self, item):
        """头插法"""
        node = Node(item)
        if self.is_empty():
            self.__head = node
        else:
            node.next = self.__head
            self.__head.prev = node # __head指向节点的前驱节点指向node
            self.__head = node
    def append(self, item):
        """尾插法"""
        pass
    def insert(self, pos, item):
        """指定位置添加"""
        pass
    def remove(self, item):
        """删除节点"""
        pass
    def search(self, item):
        """查找节点是否存在"""
        pass