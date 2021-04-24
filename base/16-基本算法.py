import random


def bubble_sort(a: list) -> None:
    """
    冒泡排序
    :param a:
    :return:
    """
    for i in range(0, len(a) - 1):
        is_exchange = False
        for j in range(0, len(a) - 1 - i):
            if a[j] > a[j + 1]:
                temp = a[j + 1]
                a[j + 1] = a[j]
                a[j] = temp
                is_exchange = True
        if not is_exchange:
            break
        else:
            is_exchange = False
    print("排序后", a)


def select_sort(a: list) -> None:
    """
    选择排序
    :param a:
    :return:
    """
    for i in range(len(a)):
        temp = i
        for j in range(i + 1, len(a)):
            if a[j] < a[temp]:
                temp = j
        if temp != i:
            t = a[temp]
            a[temp] = a[i]
            a[i] = t
    print("排序后", a)


def insert_sort(a: list) -> None:
    """
    插入排序
    :param a:
    :return:
    """
    for i in range(1, len(a)):
        temp = a[i]
        index = i - 1;
        while a[index] > temp and index >=0:
            a[index+1] = a[index]
            index = index - 1

        a[index+1] = temp




def shell_sort(a: list) -> None:
    """
    希尔排序
    :param a:
    :return:
    """
    pass


def quick_sort(a: list) -> None:
    """
   快速排序
   :param a:
   :return:
   """

    def partition(a: list, lo: int, hi: int) -> int:
        key = a[lo]
        while lo < hi:
            while lo < hi and a[hi] >= key:
                hi = hi - 1
            a[lo] = a[hi]
            while lo < hi and a[lo] <= key:
                lo = lo + 1
            a[hi] = a[lo]
        a[lo] = key
        return lo

    def sort(a: list, lo: int, hi: int) -> None:
        if lo >= hi:
            return
        index = partition(a, lo, hi)
        sort(a, lo, index - 1)
        sort(a, index + 1, hi)

    sort(a, 0, len(a) - 1)
    print("排序后", a)


def merge_sort(a: list) -> None:
    """
    归并排序
    :param a:
    :return:
    """

    def divide(a: list, left: int, right: int, temp: list) -> None:
        if left >= right:
            return
        mid = (left + right) // 2
        divide(a, left, mid, temp)
        divide(a, mid + 1, right, temp)
        merge(a, mid, left, right, temp)

    def merge(a: list, mid: int, left: int, right: int, temp: list) -> None:

        r = mid + 1;
        l = left
        point = 0
        while l <= mid and r <= right:
            if a[l] < a[r]:
                temp[point] = a[l]
                l = l + 1
            else:
                temp[point] = a[r]
                r = r + 1
            point = point + 1
        while l <= mid:
            temp[point] = a[l]
            l = l + 1
            point = point + 1
        while r <= right:
            temp[point] = a[r]
            r = r + 1
            point = point + 1

        for i in range(point):
            a[left] = temp[i]
            left = left + 1

    divide(a, 0, len(a) - 1, [0] * len(a))
    print("排序后", a)


def heap_sort(a: list) -> None:
    """
    堆排序
    :param a:
    :return:
    """
    pass


def radix_sort(a: list) -> None:
    """
    桶排序
    :param a:
    :return:
    """
    pass


def init() -> list:
    a = []
    for i in range(10):
        a.append(random.randint(1, 30))
    print("排序前", a)
    return a


arr = init()
bubble_sort(arr)

arr = init()
select_sort(arr)

arr = init()
quick_sort(arr)

arr = init()
merge_sort(arr)
