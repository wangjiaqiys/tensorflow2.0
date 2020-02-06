# _*_ coding:utf-8 _*_
#
#   author:
# 
#   func: quick sort

def quick_sort(alist, first, last):
    """快速排序"""
    if first >= last:
        return
    mid_value = alist[first]
    low = first
    high = last
    while low < high:
        # TODO: value = mid_valu
        ## 加上等号，相当于把相等的值放在右边
        # high 游标左移
        while low < high and alist[high] >= mid_value: # high 指针一直往左走
            high -= 1
        alist[low] = alist[high]
        
        # low 游标右移
        while low < high and alist[low] < mid_value:
            low += 1
        alist[high] = alist[low]
    # 从循环退出时, low==high
    alist[low] = mid_value

    # 对 low 左边的列表执行快速排序
    quick_sort(alist, first, low-1)
    # 对 low 右边的列表执行快递排序
    quick_sort(alist, low+1, last)
    
if __name__ == "__main__":
    li = [54, 26, 93, 17, 77, 31, 44, 55, 20, 54]
    print(li)
    print('* '*20)
    quick_sort(li, 0, len(li)-1)
    print(li)
