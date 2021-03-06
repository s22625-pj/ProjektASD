import time
from tab1 import tab1
from tab2 import tab2
from tab3 import tab3

def partition(l, r, nums):

    pivot, ptr = nums[r], l
    for i in range(l, r):
        if nums[i] <= pivot:
            nums[i], nums[ptr] = nums[ptr], nums[i]
            ptr += 1

    nums[ptr], nums[r] = nums[r], nums[ptr]
    return ptr  
 
def quick_sort(l, r, nums):
    if len(nums) == 1:
        return nums
    if l < r:
        pi = partition(l, r, nums)
        quick_sort(l, pi-1, nums)
        quick_sort(pi+1, r, nums) 
    return nums
 
tab4 = [5,52,52,13,65,23,41,59,71,4,17,72,52,13,65,23,41,59,71,4,17,72,52,13,65,23,41,59,71,4,17,72,52,13,65,23,41,59,71,4,17,72,52,13,65,23,41,59,71,4,17,72,52,13,65,23,41,59,71,4,17,72,52,13,65,23,41,59,71,4,17,72,52,13,65,23,41,59,71,4,17,72,52,13,65,23,41,59,71,4,17,72,52,13,65,23,41,59,71,4,17,72,52,13,65,23,41,59,71,4,17,72,52,13,65,23,41,59,71,4,17,72,52,13,65,23,41,59,71,4,17,72,52,13,65,23,41,59,71,4,17,72,52,13,65,23,41,59,71,4,17,72,52,13,65,23,41,59,71,4,17,72,52,13,65,23,41,59,71,4,17,72,52,13,65,23,41,59,71,4,17,72,52,13,65,23,41,59,71,4,17,72,52,13,65,23,41,59,71,4,17,72,52,13,65,23,41,59,71,4,17,72,52,13,65,23,41,59,71,4,17,72,52,13,65,23,41,59,71,4,17,72,52,13,65,23,41,59,71,4,17,72,52,13,65,23,41,59,71,4,17,72,52,13,65,23,41,59,71,4,17,72,52,13,65,23,41,59,71,4,17,72,52,13,65,23,41,59,71,4,17,72,52,13,65,23,41,59,71,4,17,72,52,13,65,23,41,59,71,4,17,72,52,13,65,23,41,59,71,4,17,72,52,13,65,23,41,59,71,4,17,72,52,13,65,23,41,59,71,4,17,72,52,13,65,23,41,59,71,4,17,72,52,13,65,23,41,59,71,4,17,72,52,13,65,23,41,59,71,4,17,72,52,13,65,23,41,59,71,4,17,72,52,13,65,23,41,59,71,4,17,72,52,13,65,23,41,59,71,4,17,72,52,13,65,23,41,59,71,4,17,72,52,13,65,23,41,59,71,4,17,72,52,13,65,23,41,59,71,4,17,72,52,13,65,23,41,59,71,4,17,72,52,13,65,23,41,59,71,4,17,72,52,13,65,23,41,59,71,4,17,72,52,13,65,23,41,59,71,4,17,72,52,13,65,23,41,59,71,4,17,72,52,13,65,23,41,59,71,4,17,72,52,13,65,23,41,59,71,4,17,72,52,13,65,23,41,59,71,4,17,72,52,13,65,23,41,59,71,4,17,72,52,13,65,23,41,59,71,4,17,72,13,65,23,41,59,71,4,17,72]

start_time = time.time()
quick_sort(0, len(tab1)-1, tab1)
end_time = time.time()
print("Czas wykonania",end_time-start_time)

start_time = time.time()
quick_sort(0, len(tab2)-1, tab2)
end_time = time.time()
print("Czas wykonania",end_time-start_time)

start_time = time.time()
quick_sort(0, len(tab3)-1, tab3)
end_time = time.time()
print("Czas wykonania",end_time-start_time)

# start_time = time.time()
# quick_sort(0, len(tab4)-1, tab4)
# end_time = time.time()
# print("Czas wykonania",end_time-start_time)