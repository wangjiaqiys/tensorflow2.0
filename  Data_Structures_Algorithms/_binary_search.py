# _*_ coding:utf-8 _*_
#
#   author:
#
#   二分查找
def binary_search(alist, item):
    """递归 - 二分查找"""
    n = len(alist)
    if n > 0:
        mid = n//2 # 中间位置
        if alist[mid] == item:
            return True
        elif item < alist[mid]:
            return binary_search(alist[:mid], item)
        else:
            return binary_search(alist[mid+1:], item)
    return False

def binary_search_1(alist, item):
    """非递归 - 二分查找"""
    n = len(alist)
    first = 0
    last = n-1
    while first <= last:
        mid = (first + last) // 2
        if alist[mid] == item:
            return True
        elif item < alist[mid]:
            # first = 0
            last = mid -1
        else:
            first = mid + 1
    return False

if __name__ == '__main__':
    li = [17, 20, 26, 31, 44, 54, 55, 77, 93]
    print(binary_search(li, 55))
    print(binary_search(li, 50))
    print(binary_search_1(li, 55))