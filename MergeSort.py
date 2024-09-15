from Task1 import RandomArray
import time
import csv

def MergeSort(array, start, end):
    if(end - start <= 1): 
        return array
    else:
        m = (start + end) // 2
        MergeSort(array, start, m)
        MergeSort(array, m, end)

        Merge(array, start, m, end)
    
def Merge(array, p, q, r):
    left_array = array[p:q]
    right_array = array[q:r]

    i, j, k = 0, 0, p

    while i < len(left_array) and j < len(right_array):
        if left_array[i] <= right_array[j]:
            array[k] = left_array[i]
            i += 1
        else:
            array[k] = right_array[j]
            j += 1
        k += 1

    while i < len(left_array):
        array[k] = left_array[i]
        i += 1
        k += 1

    while j < len(right_array):
        array[k] = right_array[j]
        j += 1
        k += 1

if __name__ == "__main__":
   
    Arraysize = 300
    ObtainedArray = RandomArray(Arraysize)
    start_time = time.time()
    MergeSort(ObtainedArray, 0, Arraysize)
    end_time = time.time()
    runtime = end_time - start_time
    print("Runtime of MergeSort is", runtime, "seconds")

    with open('SortedMergeSort.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        for number in ObtainedArray:
            writer.writerow([number])

    print("Sorted array saved to SortedMergeSort.csv")
