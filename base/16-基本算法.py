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
                a[j], a[j + 1] = a[j + 1], a[j]
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
            a[temp], a[i] = a[i], a[temp]

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
        while a[index] > temp and index >= 0:
            a[index + 1] = a[index]
            index = index - 1

        a[index + 1] = temp

    print("排序后", a)


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

    def init_heap(a: list) -> None:
        for i in range(len(a) // 2 - 1, -1, -1):
            adjust_heap(a, i, len(a))

    def adjust_heap(a: list, index: int, length: int) -> None:

        if index >= length:
            return

        left = 2 * index + 1
        right = 2 * index + 2
        max = index
        if left < length and a[max] < a[left]:
            max = left

        if right < length and a[max] < a[right]:
            max = right
        if max != index:
            a[max], a[index] = a[index], a[max]
            adjust_heap(a, max, length)

    def build_heap(a: list, n: int) -> None:
        for i in range(n // 2 - 1, -1, -1):
            adjust_heap(a, i, n)

    def sort(a: list) -> None:
        init_heap(a)
        for i in range(len(a) - 1, 0, -1):
            a[i], a[0] = a[0], a[i]
            build_heap(a, i)

    sort(a)
    print("排序后", a)


def radix_sort(a: list) -> None:
    """
    桶排序
    :param a:
    :return:
    """
    bucket = [[i for i in range(10)] for i in range(10)]
    bucket_count = [0] * 10

    max_num = -1
    for i in a:
        if i > max_num:
            max_num = i

    count = len(str(max_num))
    step = 1

    while count > 0:
        for i in range(len(a)):
            res = a[i] // step % 10
            bucket[res][bucket_count[res]] = a[i]
            bucket_count[res] = bucket_count[res] + 1

        t = 0
        for i in range(10):
            for k in range(bucket_count[i]):
                a[t] = bucket[i][k]
                t = t + 1
            bucket_count[i] = 0

        count = count - 1
        step = step * 10
    print("排序后", a)


def init() -> list:
    a = []
    for i in range(10):
        a.append(random.randint(1, 1000))
    print("排序前", a)
    return a


arr = init()
bubble_sort(arr)

arr = init()
select_sort(arr)

arr = init()
insert_sort(arr)

arr = init()
quick_sort(arr)

arr = init()
merge_sort(arr)

arr = init()
heap_sort(arr)

arr = init()
radix_sort(arr)
