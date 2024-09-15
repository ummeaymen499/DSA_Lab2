from Task1 import RandomArray
from Insertion import InsertionSort
from MergeSort import Merge
import time
import csv

def HybridMergeSort(array, start, end):
    Limit = 50  
    if end - start <= Limit:
        InsertionSort(array, start, end)
    else:
        if end - start > 1:
            mid = (start + end) // 2
            HybridMergeSort(array, start, mid)
            HybridMergeSort(array, mid, end)
            Merge(array, start, mid, end)
            
if __name__ == "__main__":
    Arraysize = 30000
    ObtainedArray = RandomArray(Arraysize)
    start_time = time.time()
    HybridMergeSort(ObtainedArray, 0, Arraysize)
    end_time = time.time()
    runtime = end_time - start_time
    print("Runtime of HybridMergeSort is", runtime, "seconds")
    
    with open('SortedHybridSort.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        for number in ObtainedArray:
            writer.writerow([number])

    print("Sorted array saved to SortedHybridSort.csv")
