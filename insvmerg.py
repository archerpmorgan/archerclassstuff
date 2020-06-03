import numpy as np
import datetime
from tabulate import tabulate
 
# Function to do insertion sort 
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


# Python program for implementation of MergeSort
# source: https://www.geeksforgeeks.org/merge-sort/
def mergeSort(arr): 
    if len(arr) >1: 
        mid = len(arr)//2 #Finding the mid of the array 
        L = arr[:mid] # Dividing the array elements  
        R = arr[mid:] # into 2 halves 
  
        mergeSort(L) # Sorting the first half 
        mergeSort(R) # Sorting the second half 
  
        i = j = k = 0
          
        # Copy data to temp arrays L[] and R[] 
        while i < len(L) and j < len(R): 
            if L[i] < R[j]: 
                arr[k] = L[i] 
                i+=1
            else: 
                arr[k] = R[j] 
                j+=1
            k+=1
          
        # Checking if any element was left 
        while i < len(L): 
            arr[k] = L[i] 
            i+=1
            k+=1
          
        while j < len(R): 
            arr[k] = R[j] 
            j+=1
            k+=1
  


def main():

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
        mergeSort(arr)
        stop = datetime.datetime.now()
        sort_time = stop - start 
        merge_times.append(sort_time)

    table = [insertion_times, merge_times]

    print(tabulate(table, headers))




if __name__ == "__main__":
    main()