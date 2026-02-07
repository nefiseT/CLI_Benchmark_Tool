#main algorithmss

import sys
sys.setrecursionlimit(10000)

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = []
    for x in arr:
        if x < pivot:
            left.append(x)

    middle = [x for x in arr if x == pivot]

    right = []
    for x in arr:
        if x > pivot:
            right.append(x)

    return quick_sort(left) + middle + quick_sort(right)

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i -1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

