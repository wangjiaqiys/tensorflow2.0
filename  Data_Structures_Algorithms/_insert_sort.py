# _*_ coding:utf-8 _*_
def select_sort(alist):
    """选择排序"""
    n = len(alist)
    for j in range(1, n):
        i = j
        while i > 0:
            if alist[i] < alist[i-1]:
                alist[i], alist[i-1] = alist[i-1], alist[i]
            i -= 1
            # else:
            #     break
    return alist
if __name__ == '__main__':
    print(select_sort([1, 2, 1, 3, 1, 0, -1, -2, 1, 0, 2, 4]))
    print(select_sort([0, 1, 2, 5, 4]))    