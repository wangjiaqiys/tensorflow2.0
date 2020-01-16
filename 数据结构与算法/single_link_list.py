# _*_ coding:utf-8 _*_
"""
链表(抽象为线性表)
-1. 为什么需要链表
顺序表的构建需要预先知道数据大小来申请连续的存储空间, 而在进行扩充时又需要进行数据的搬迁, 所以使用起来并不是很灵活;
链表结构可以充分利用计算机内存空间, 实现灵活的内存动态管理.
-2. 链表的定义 - <类似一根线串起来所有数据, 上升到二维, 就是树, 再上升, 就是图>
LinkedList 是一种常见的基础数据结构, 是一种线性表, 但是不像顺序表一样连续存储数据, 
而是在每一个节点(数据存储单元)里存放下一个节点的位置信息(即地址)
分为 数据区 | 链接区(指针区)
-3. 分类
--1. 单向链表: 也叫单链表, 是链表中最简单的一种形式, 它的每个节点包含两个域, 一个信息域(元素域)和一个链接域<next>.
这个链接指向链表中的下一个节点, 而最后一个节点的链接则指向一个空值:
    * 表元素域elem用来存放具体的数据
    * 链接域next用来存放下一个节点的位置
    * 变量p指向链表的头节点(首节点)的位置, 从p出发能找到表中的任意节点
单链表的操作:
    * is_empty() 链表是否为空
    * length() 链表长度
    * travel() 遍历整个链表
    * add(item) 链表头部添加元素
    * append(item) 链表尾部添加元素
    * insert(pos, item) 指定位置添加元素
    * remove(item) 删除节点
    * search(item) 查找节点是否存在 
后继节点: 指的就是 cur.next
"""

# 单链表的实现: 实现需要明白一方面解决数据保存问题,另一方面是数据的操作
class singleNode(object):
    """单链表的节点"""
    def __init__(self, item):
        # _item存放数据元素
        self.item = item 
        # _next是下一个节点的标识
        self.next = None
class SingleLinkList(object):
    """单链表"""        
    def __init__(self, node=None):
        self.__head = node # 私有属性,head指针不需要对外<私有变量主要双下划线>
    def is_empty(self):
        """判断链表是否为空"""
        return self.__head == None
    def length(self):
        """返回链表的长度"""
        # 需要完成从头到尾的遍历
        # 游标指针 cur, 从 __head开始, 看下一个节点的next是多少
        cur = self.__head # 初始状态
        # count 记录数量
        count = 0
        while cur != None:
            count += 1
            cur = cur.next 
        return count
    def travel(self): 
        """遍历链表"""
        # 游标指针
        cur = self.__head
        while cur != None: # 使用None这个条件, 如果最后一个节点是None, 那么遍历的时候就会丢掉最后一个数据
            print(cur.item, end=" ")
            cur = cur.next
        print(' ')
        pass
    def add(self, item):
        """头部添加元素, 叫做<头插法>"""
        # __head要指向新节点, 新节点的指针要指向先前__head指向的node
        # 新节点作为头部
        # 这里对于self.__head如果是None也适用
        node = singleNode(item) 
        # node.next, self.__head = self.__head, node (这个也没问题,要注意赋值顺序)
        node.next = self.__head # node.next指向头部, 相当于把链表串联起来(保序)
        self.__head = node # 然后再将头部赋值为node, 即获得最后链表

    def append(self, item):
        """尾部添加元素, 叫做<尾插法>"""
        # 构造节点
        node = singleNode(item)
        if self.is_empty():
            self.__head = node
        else:
            # 尾节点的next指向node
            cur = self.__head # 如果是空链表, 需要让__head直接指向新添加的节点
            while cur.next != None:
                cur = cur.next
            cur.next = node
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
            node = singleNode(item)
            count = 0
            pre = self.__head
            while count < (pos-1):
                count += 1
                pre = pre.next # 向后移动,移动到插入位置的前一个位置
            node.next = pre.next # 新节点指向插入前一个节点的后节点
            pre.next = node # 前一个节点指向新节点
    def remove(self, item):
        """删除节点
        eg: 2 3 2 3 remove 2 -> 3 2 3
        删除节点, 该节点的前一个节点还需要指向删除节点的后一个节点
        <pre.next = cur.next> -> <pre.next = pre.next.next>
        """
        cur = self.__head 
        pre = None
        while cur != None:
            if cur.item == item:
                # 特殊情况
                ## 1. 先判断此节点是否是头节点
                ### 如果是头节点, self.__head 就要往下指
                if cur == self.__head:
                    self.__head = cur.next
                    break
                else:
                    pre.next = cur.next
                    break
            else:
                pre = cur # 开始移动游标
                cur = cur.next 
    def search(self, item):
        """查找节点是否存在"""
        # 特殊情况就是self.__head = None 情况
        cur = self.__head # 游标指针,从头节点开始进行比对
        while cur != None:
            if cur.item == item:
                return True
            else:
                cur = cur.next
        return False
if __name__ == '__main__':
    sll = SingleLinkList() # 空链表
    print(sll.is_empty())
    print(sll.length())
    print('*'*10)

    sll.append(1)
    print(sll.is_empty())
    print(sll.length())
    print('*'*10)
    
    sll.append(2)
    sll.append(3)
    sll.append(4)
    sll.append(5)
    sll.append(6)
    print(sll.length())
    sll.travel()

    print('*'*10)
    sll.add(0)
    print(sll.length())
    sll.travel()

    print('*'*10)
    sll.insert(6, 1)
    sll.travel()

    print('*'*10)
    print(sll.search(100))

    print('*'*10)
    sll.remove(1)
    sll.travel()
    print('*'*10)
    sll.remove(6)
    sll.travel()