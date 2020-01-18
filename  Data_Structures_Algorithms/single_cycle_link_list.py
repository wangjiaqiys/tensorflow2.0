# _*_ coding:utf-8 _*_
"""
单向循环链表: 最后一个节点的next指针指向头节点
单链循环表的操作:
    * is_empty() 链表是否为空
    * length() 链表长度
    * travel() 遍历整个链表
    * add(item) 链表头部添加元素
    * append(item) 链表尾部添加元素
    * insert(pos, item) 指定位置添加元素
    * remove(item) 删除节点
    * search(item) 查找节点是否存在 
"""

# 单链表的实现: 实现需要明白一方面解决数据保存问题,另一方面是数据的操作
class Node(object):
    """节点"""
    def __init__(self, item):
        # _item存放数据元素
        self.item = item 
        # _next是下一个节点的标识
        self.next = None
class SingleCycleLinkList(object):
    """单向循环表"""        
    def __init__(self, node=None):
        self.__head = node # 私有属性,head指针不需要对外<私有变量主要双下划线>
        if node:
            node.next = node
    def is_empty(self):
        """判断链表是否为空"""
        return (self.__head is None)
    def length(self):
        """返回链表的长度"""
        # 需要完成从头到尾的遍历
        # 游标指针 cur, 从 __head开始, 看下一个节点的next是多少
        if self.is_empty():
            return 0
        cur = self.__head # 初始状态
        # count 记录数量
        count = 1
        while cur.next != self.__head: # 指向同一个内存区
            count += 1 
            cur = cur.next 
        return count
    def travel(self): 
        """遍历链表"""
        # 游标指针
        if self.is_empty():
            return 
        cur = self.__head
        while cur.next != self.__head: # 使用None这个条件, 如果最后一个节点是None, 那么遍历的时候就会丢掉最后一个数据
            print(cur.item, end=" ")
            cur = cur.next
        # 退出循环, cur指向尾节点, 但尾节点的元素未打印
        print(cur.item)
        print(' ')
        pass
    def add(self, item):
        """头部添加元素, 叫做<头插法>"""
        # __head要指向新节点, 新节点的指针要指向先前__head指向的node
        # 新节点作为头部
        # 这里对于self.__head如果是None也适用
        node = Node(item) 
        if self.is_empty():
            self.__head = node 
            node.next = node 
        else:
            cur = self.__head 
            while cur.next != self.__head:
                cur = cur.next 
            node.next = self.__head # node.next指向头部, 相当于把链表串联起来(保序)
            self.__head = node # 然后再将头部赋值为node, 即获得最后链表
            cur.next = node
    def append(self, item):
        """尾部添加元素, 叫做<尾插法>"""
        # 构造节点
        node = Node(item)
        if self.is_empty():
            self.__head = node
            node.next = node
        else:
            # 尾节点的next指向node
            cur = self.__head # 如果是空链表, 需要让__head直接指向新添加的节点
            while cur.next != self.__head:
                cur = cur.next
            cur.next = node
            node.next = self.__head # <=> node.next = cur.next
    def insert(self, pos, item):
        """指定位置添加元素
        :param pos 从0开始
        """
        # pos 的前一个node指向新添加的node
        # 新添加的node指向之前后面的node
        if pos <= 0: # 头插法
            self.add(item)
        elif pos > (self.length()-1): # 尾部添加
            self.append(item)
        else:
            node = Node(item)
            count = 0
            cur = self.__head
            while count < (pos-1):
                count += 1
                cur = cur.next # 向后移动,移动到插入位置的前一个位置
            node.next = cur.next # 新节点指向插入前一个节点的后节点
            cur.next = node # 前一个节点指向新节点
    def remove(self, item):
        """删除节点
        eg: 2 3 2 3 remove 2 -> 3 2 3
        删除节点, 该节点的前一个节点还需要指向删除节点的后一个节点
        <pre.next = cur.next> -> <pre.next = pre.next.next>
        """
        if self.is_empty():
            return 
        cur = self.__head 
        pre = None
        while cur.next != self.__head:
            if cur.item == item:
                # 特殊情况
                ## 1. 先判断此节点是否是头节点
                ### 如果是头节点, self.__head 就要往下指
                if cur == self.__head: # 这里的特殊情况就是尾节点
                    # 头节点的情况
                    # 找尾节点
                    rear = self.__head
                    while rear.next != self.__head:
                        rear = rear.next 
                    self.__head = cur.next 
                    rear.next = self.__head
                else:
                    # 中间节点
                    pre.next = cur.next # 这句话对于尾部不可以处理
                return
            else:
                pre = cur # 开始移动游标
                cur = cur.next 
        # 退出循环, cur指向尾节点
        if cur.item == item:
            # if self.length() == 1: # cur == self.__head <链表只有一个节点>
            if cur == self.__head:
                self.__head = None
            else:
                pre.next = cur.next
    def search(self, item):
        """查找节点是否存在"""
        # 特殊情况就是self.__head = None 情况
        if self.is_empty():
            return False 
        cur = self.__head # 游标指针,从头节点开始进行比对
        while cur.next != self.__head:
            if cur.item == item:
                return True
            else:
                cur = cur.next
        # 考虑尾部
        if cur.item == item:
            return True
        return False
if __name__ == '__main__':
    scll = SingleCycleLinkList() # 空链表
    print(scll.is_empty())
    print(scll.length())
    print('*'*10)

    scll.append(1)
    print(scll.is_empty())
    print(scll.length())
    print('*'*10)
    
    scll.append(2)
    scll.append(3)
    scll.append(4)
    scll.append(5)
    scll.append(6)
    print(scll.length())
    scll.travel()

    print('*'*10)
    scll.add(0)
    print(scll.length())
    scll.travel()

    print('*'*10)
    scll.insert(6, 1)
    scll.travel()

    print('*'*10)
    print(scll.search(100))

    print('*'*10)
    scll.remove(1)
    scll.travel()
    print('*'*10)
    scll.remove(6)
    scll.travel()