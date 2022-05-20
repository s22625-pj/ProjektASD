import time
from tab1 import tab1
from tab2 import tab2
from tab3 import tab3

def merge_sort(array):
    if len(array) > 1:
        mid = len(array) // 2
        left = array[:mid]
        right = array[mid:]

        merge_sort(left)
        merge_sort(right)

        i = 0 
        j = 0 
        k = 0 

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                array[k] = left[i]
                i += 1
            else:
                array[k] = right[j]
                j += 1 
            k += 1

        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1

        while j < len(left):
            array[k] = right[j]
            j += 1
            k += 1

start_time = time.time()
merge_sort(tab1)
end_time = time.time()
print("Czas wykonania",end_time-start_time)

start_time = time.time()
merge_sort(tab2)
end_time = time.time()
print("Czas wykonania",end_time-start_time)

start_time = time.time()
merge_sort(tab3)
end_time = time.time()
print("Czas wykonania",end_time-start_time)