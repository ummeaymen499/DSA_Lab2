from Task1 import RandomArray
import time
import csv
def InsertionSort(array,start,end):
    for j in range(start+1,end):
        key=array[j]
        i=j-1
        while i>=start and array[i]>key:
            array[i+1]=array[i]
            i=i-1 
        array[i+1]=key

if __name__=="__main__":
   
    Arraysize=30000
    ObtainedArray=RandomArray(Arraysize)
    start_time=time.time()
    InsertionSort(ObtainedArray,0,Arraysize)
    end_time=time.time()
    runtime=end_time-start_time
    print("Runtime of InsertionSort is ",runtime," seconds")     

    with open('SortedInsertionSort.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        for number in ObtainedArray:
            writer.writerow([number])

    print("Sorted array saved to SortedInsertionSort.csv") 
