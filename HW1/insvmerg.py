import numpy as np
import datetime
from tabulate import tabulate
 
# source: https://www.geeksforgeeks.org/python-program-for-insertion-sort/
def insertionSort(arr): 
  
    # Traverse through 1 to len(arr) 
    for i in range(1, len(arr)): 
  
        key = arr[i] 
  
        # Move elements of arr[0..i-1], that are 
        # greater than key, to one position ahead 
        # of their current position 
        j = i-1
        while j >=0 and key < arr[j] : 
                arr[j+1] = arr[j] 
                j -= 1
        arr[j+1] = key 

# source https://www.geeksforgeeks.org/python-program-for-merge-sort/
def merge(arr, l, m, r): 
    n1 = m - l + 1
    n2 = r- m 
  
    L = [0] * (n1) 
    R = [0] * (n2) 
  
    for i in range(0 , n1): 
        L[i] = arr[l + i] 
  
    for j in range(0 , n2): 
        R[j] = arr[m + 1 + j] 
  
    i = 0 
    j = 0   
    k = l  
  
    while i < n1 and j < n2 : 
        if L[i] <= R[j]: 
            arr[k] = L[i] 
            i += 1
        else: 
            arr[k] = R[j] 
            j += 1
        k += 1
  
    while i < n1: 
        arr[k] = L[i] 
        i += 1
        k += 1
  
    while j < n2: 
        arr[k] = R[j] 
        j += 1
        k += 1
  
def mergeSort(arr, l, r): 
    if l < r: 
        m = (l+(r-1))//2
        mergeSort(arr, l, m) 
        mergeSort(arr, m+1, r) 
        merge(arr, l, m, r) 
  
 # version which uses insertion sort for when k is in [10,25]
def mergeSortCoarse(arr, l, r):
    if l < r: 
        if len(arr) <= 25 and len(arr) >= 10:
            insertionSort(arr)
        else:
            m = (l+(r-1))//2
            mergeSort(arr, l, m) 
            mergeSort(arr, m+1, r) 
            merge(arr, l, m, r) 

def is_sorted(a):
    for i in range(a.size-1):
         if a[i+1] < a[i]:
               return False
    return True

def sort_works_merge(sort):
    arr = np.random.rand(2**5)
    sort(arr, 0, len(arr)-1)
    if is_sorted(arr):
        return True 
    else:
        return False

def sort_works(sort):
    arr = np.random.rand(2**5)
    sort(arr)
    if is_sorted(arr):
        return True 
    else:
        return False


def main():

    #make sure the sorts work
    if not sort_works(insertionSort):
        print("Insertion Sort doesn't work")
        return
    if not sort_works_merge(mergeSort):
        print("Merge Sort doesn't work")
        return
    if not sort_works_merge(mergeSortCoarse):
        print("Coarse Merge Sort doesn't work")
        return

    # experiment 1, find optimal k

    insertion_times = ["Insertion Sort"]
    merge_times = ["Merge Sort"]
    headers = ["Sort Type"]

    for i in range(2,14):
        arr = np.random.rand(2**i)
        arr2 = np.copy(arr)

        headers.append(str(2**i))

        # sort list of length 2**i with insertion sort
        start = datetime.datetime.now()
        insertionSort(arr)
        stop = datetime.datetime.now()
        sort_time = stop - start 
        insertion_times.append(sort_time)

        # sort list of length 2**i with merge sort
        start = datetime.datetime.now()
        mergeSort(arr, 0, len(arr)-1)
        stop = datetime.datetime.now()
        sort_time = stop - start 
        merge_times.append(sort_time)

    table = [insertion_times, merge_times]
    print(tabulate(table, headers))

    merge_times = ["Merge Sort"]
    merge_coarse_times = ["Coarse Merge Sort"]
    headers = ["Sort Type"]

    # experiment 2, compare merge sort with merge sort that uses insertion sort

    for i in range(2,24):
        arr = np.random.rand(2**i)
        arr2 = np.copy(arr)

        headers.append(str(2**i))

        # sort list of length 2**i with insertion sort
        start = datetime.datetime.now()
        mergeSort(arr, 0, len(arr)-1)
        stop = datetime.datetime.now()
        sort_time = stop - start 
        merge_times.append(sort_time)

        # sort list of length 2**i with merge sort
        start = datetime.datetime.now()
        mergeSortCoarse(arr, 0, len(arr)-1)
        stop = datetime.datetime.now()
        sort_time = stop - start 
        merge_coarse_times.append(sort_time)

    table = [merge_times, merge_coarse_times]
    print(tabulate(table, headers))



if __name__ == "__main__":
    main()