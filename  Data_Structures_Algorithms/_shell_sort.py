# _*_ coding:utf-8 _*_
# 希尔排序
def shell_sort(alist):
    """希尔排序"""
    n = len(alist)
    gap = n // 2 # 每次按照折半的方式
    while gap >= 1:
        for j in range(gap, n):
            i = j
            while i > 0:
                if alist[i] < alist[i-gap]: # 插入排序中减1, 相当于gap
                    alist[i-gap], alist[i] = alist[i], alist[i-gap]
                i -= gap
        gap //= 2
    return alist

if __name__ == '__main__':
    print(shell_sort([-1, -2, 0, 1, 3, 2, -1, -2, -3]))
    