# _*_ coding:utf-8 _*_
"""
栈(stack), 或者堆栈:
概念: 是一种容器, 可存放数据元素, 访问元素, 删除元素;
特点: 只能允许在容器的一端(栈顶)进行加入数据(push), 和输出数据(pop), 即后进先出(Last In First Out)
实现: 栈可以用顺序表实现, 也可以用链表实现

栈的操作:
1. Stack() 创建一个新的空栈
2. push(item) 添加一个新的元素item到栈顶 <压栈/入栈>
3. pop() 弹出栈顶元素 <出栈>
4. peek() 返回栈顶元素
5. is_empty() 判断栈是否为空
6. size() 返回栈的元素个数
"""
class Stack():
    def __init__(self):
        self.__list = [] # 私有变量
    def push(self, item):
        """添加一个新的元素item到栈顶"""
        self.__list.append(item) # 通过尾部添加
        # self.__list.insert(0, item) # 但是通过头部, 操作复杂度是O(n)
    def pop(self):
        """弹出栈顶元素""" 
        return self.__list.pop() # 从尾部弹出
        # self.__list.pop(0)
    def peek(self):
        """"返回栈顶元素"""
        if self.__list:
            return self.__list[-1]
        else:
            return None
    def is_empty(self):
        """判断栈是否为空"""
        return self.__list == []
    def size(self):
        """返回栈的元素个数"""
        return len(self.__list)

if __name__ == '__main__':
    s = Stack()        
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    print(s.pop())
    print(s.pop())
    print(s.pop())
    print(s.pop())