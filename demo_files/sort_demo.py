def bubble_sort(arr):
    """时间复杂度是O(n^2)，当然可以再考虑一下极端的情况：当队列已经从小到大排好序或者从大到小排好序，
    从小到大排好顺序时可以只扫描一遍就结束排序，此时时间复杂度为O(n)，如果是从大到小，
    那么就需要扫描n-1次，同时需要比较交换n-1次，时间复杂度为O(n^2)"""
    length = len(arr)
    for i in range(length - 1):
        for j in range(length - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def selection_sort(arr):
    """选择排序 - 稳定性:不稳定,因为存在任意位置的两个元素交换，比如[5,  8, 5, 2]，
    第一个5会和2交换位置，所以改变了两个5原来的相对顺序，所以为不稳定排序, O(n^2)"""
    length = len(arr)
    count = 0
    for i in range(length - 1):
        # 将起始元素设为最小元素
        min_index = i
        for j in range(i + 1, length):
            if arr[j] < arr[min_index]:
                min_index = j
                count += 1
        # 查找一遍后将最小元素与起始元素互换
        arr[min_index], arr[i] = arr[i], arr[min_index]
    print(count)
    return arr


def insert_sort(arr):
    '''插入排序 -- 和冒泡排序几乎一样'''
    length = len(arr)
    for i in range(1, length):
        # 从第i个元素开始向前比较，如果小于前一个元素，交换位置
        for j in range(i, 0, -1):
            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
    return arr


def quick_sort(arr):
    """快速排序"""
    length = len(arr)
    if length < 2:  # 递归的出口
        return arr
    mid = arr[length // 2]  # 选取基准值，也可以选取第一个或最后一个元素
    left, right = [], []  # 定义基准值左右两侧的列表
    arr.remove(mid)  # 从原始数组中移除基准值
    for num in arr:
        if num >= mid:
            right.append(num)
        else:
            left.append(num)
    return quick_sort(left) + [mid] + quick_sort(right)


# 二分查找适用于有序的序列，通过将序列不断的对折分为区间，从而确定查找值是否存在，优点是速度快
def binary_chop(alist, data):
    '''二分查找-递归,时间复杂度O(logn),二分查找是有条件的,第一要求有序,
    其次因为二分查找操作的是下标,所以要求是顺序表'''
    n = len(alist)
    if n < 1:
        return False
    mid = n // 2
    if alist[mid] > data:
        return binary_chop(alist[0:mid], data)
    elif alist[mid] < data:
        return binary_chop(alist[mid + 1:], data)
    else:
        return True


# 二分查找 - 非递归
def binary_search(alist, data):
    """
    非递归解决二分查找
    :param alist:
    :return:
    """
    n = len(alist)
    first = 0
    last = n - 1
    while first <= last:
        mid = (last + first) // 2
        if alist[mid] > data:
            last = mid - 1
        elif alist[mid] < data:
            first = mid + 1
        else:
            return True
    return False


def x_sort(arr):
    n = len(arr)
    if n < 2:
        return arr
    for i in range(n):
        for j in range(i, n):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr


if __name__ == "__main__":
    # l1 = [1, 10, 2, 4, 3, 7, 5]
    import random
    l1 = [random.randint(1,10000) for _ in range(1000)]
    # print(bubble_sort(l1))
    print(selection_sort(l1))
    # print(insert_sort(l1))
    # print(quick_sort(l1))
    # l2 = quick_sort(l1)
    # print(binary_chop(l2, 6))
