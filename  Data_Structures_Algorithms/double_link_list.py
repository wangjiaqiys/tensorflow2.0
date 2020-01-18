# _*_ coding:utf-8 _*_
"""
双向链表
前驱节点 prev/prior
后继节点 next
"""
# from single_link_list import SingleLinkList
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
    def travel(self):
        """遍历链表"""
        cur = self.__head
        while cur != None:
            print(cur.item, end=" ")
            cur = cur.next
        print('')
    def add(self, item):
        """头插法"""
        node = Node(item)
        if self.is_empty():
            self.__head = node
        else:
            node.next = self.__head
            self.__head.prev = node # __head指向节点的前驱节点指向node
            self.__head = node 
            # 另一种思路 node.next.prev = node node下一个节点的前向指针指向node
    def append(self, item):
        """尾插法"""
        node = Node(item)
        if self.is_empty():
            self.__head = node
        else:
            cur = self.__head # 移动游标
            while cur.next != None:
                cur = cur.next
            cur.next = node
            node.prev = cur
    def insert(self, pos, item):
        """指定位置添加"""
        if pos <= 0:
            self.add(item)
        elif pos > (self.length()-1):
            self.append(item)
        else:
            # node.next = cur
            # node.prev = cur.prev
            # cur.prev.next = node
            # cur.prev = node
            # [1号节点] [2号节点], pos=2
            node = Node(item)
            cur = self.__head
            count = 0 
            while count < pos:
                count += 1
                cur = cur.next
            node.next = cur
            node.prev = cur.prev
            cur.prev.next = node
            cur.prev = node 
    def remove(self, item):
        """删除节点"""
        # cur.prev.next = cur.next
        # cur.next.prev = cur.prev
        cur = self.__head
        while cur != None:
            if cur.item == item:
                if cur == self.__head:
                    self.__head = cur.next
                    if cur.next: # 考虑到链表是否只有一个节点的情况
                        cur.next.prev = None
                else:
                    cur.prev.next = cur.next
                    # 考虑删除的是链表的最后一个节点
                    if cur.next:
                        cur.next.prev = cur.prev
                break
            else:
                cur = cur.next
    def search(self, item):
        """查找节点是否存在"""
        # 和单链表是一样的
        cur = self.__head # 游标指针,从头节点开始进行比对
        while cur != None:
            if cur.item == item:
                return True
            else:
                cur = cur.next
        return False
if __name__ == "__main__":
    dll = DoubleLinkList()
    print(dll.is_empty())
    print(dll.length())
    print('*'*10)

    dll.append(1)
    print(dll.is_empty())
    print(dll.length())
    print('*'*10)
    
    dll.append(2)
    dll.append(3)
    dll.append(4)
    dll.append(5)
    dll.append(6)
    print(dll.length())
    dll.travel()

    print('*'*10)
    dll.add(0)
    print(dll.length())
    dll.travel()

    print('*'*10)
    dll.insert(6, 1)
    dll.travel()

    print('*'*10)
    print(dll.search(100))

    print('*'*10)
    dll.remove(1)
    dll.travel()
    print('*'*10)
    dll.remove(6)
    dll.travel()