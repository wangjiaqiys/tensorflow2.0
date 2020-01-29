# _*_ coding:utf-8 _*_
def select_sort(alist):
    """选择排序"""
    n = len(alist)
    for j in range(n-1):
        min_index = j
        for i in range(j+1, n):
            if alist[min_index] > alist[i]:
                min_index = i 
            alist[j], alist[min_index] = alist[min_index], alist[j]
    return alist
if __name__ == '__main__':
    print(select_sort([1, 2, 1, 3, 1, 0, -1, -2, 1, 0, 2, 4]))
    print(select_sort([0, 1, 2, 3, 4]))            