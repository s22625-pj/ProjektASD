import time
from tab1 import tab1
from tab2 import tab2
from tab3 import tab3

def parent(index):
    return (index - 1) / 2

def right(parent_index):
    return 2 * parent_index + 2

def left(parent_index):
    return 2 * parent_index + 1

def heapify(A, parent_index, heap_size):
    l = left(parent_index)
    r = right(parent_index)

    if (l <= heap_size - 1) and (A[l] > A[parent_index]):
        largest = l
    else:
        largest = parent_index

    if r <= (heap_size - 1) and (A[r] > A[largest]):
        largest = r

    if largest != parent_index:

        temp = A[largest]
        A[largest] = A[parent_index]
        A[parent_index] = temp

        heapify(A, largest, heap_size)

def build_heap(A):
    start_index = len(A) // 2 - 1
    heap_size = len(A)

    for parent_index in range(start_index, -1, -1):
        heapify(A, parent_index, heap_size)

def heap_sort(A):
    build_heap(A)
    heap_size = len(A)
    for i in range(heap_size - 1, 0, -1):
        temp = A[0]
        A[0] = A[i]
        A[i] = temp
        heap_size = heap_size - 1
        heapify(A, 0, heap_size)

start_time = time.time()
heap_sort(tab1)
end_time = time.time()
print("Czas wykonania",end_time-start_time)

start_time = time.time()
heap_sort(tab2)
end_time = time.time()
print("Czas wykonania",end_time-start_time)

start_time = time.time()
heap_sort(tab3)
end_time = time.time()
print("Czas wykonania",end_time-start_time)