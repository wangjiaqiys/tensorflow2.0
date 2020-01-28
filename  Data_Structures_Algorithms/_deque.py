# _*_ coding:utf-8 _*_
"""
双端队列(deque, double-ended queue): 是一种具有队列和栈的性质的数据结构
单独看双端队列的一端, 相当于一个栈, 相当于两个栈底合在一起
"""

class Deque():
    def __init__(self):
        self.__list = []
    def add_front(self, item):
        """从对头加入一个item元素"""
        self.__list.insert(0, item)
    def add_rear(self, item):
        """从队尾加入一个item元素"""
        self.__list.append(item)
    def remove_front(self):
        """从队头删除一个item元素"""
        self.__list.pop(0)
    def remove_rear(self):
        """从队尾删除一个item元素"""
        self.__list.pop()
    def is_empty(self):
        """判断双端队列是否为空"""
        return self.__list == []
    def size(self):
        """返回队列的大小"""
        return len(self.__list)

if __name__ == "__main__":
    s = Deque()    