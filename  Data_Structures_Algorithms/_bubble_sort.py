# _*_ coding:utf-8 _*_

"""
冒泡排序:
最优时间复杂度: o(n)
最坏时间复杂度: o(n^2)
"""
def bubble_sort(alist):
    """冒泡排序"""
    for j in range(len(alist)-1): # 相当于两个指针 <n>
        count = 0 # 优化冒泡排序, 记录交换次数
        for i in range(j+1, len(alist)):
            if alist[j] > alist[i]:
                count += 1
                alist[j], alist[i] = alist[i], alist[j]
        if count == 0:
            break
    return alist

if __name__ == '__main__':
    print(bubble_sort([1, 2, 1, 3, 1, 0, -1, -2, 1, 0, 2, 4]))
    print(bubble_sort([0, 1, 2, 3, 4]))