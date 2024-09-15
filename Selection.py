from Task1 import RandomArray
import time
import csv
def SelectionSort(array,start,end):
   for i in range(start,end-1):
      min_idx=i
      for j in range(i+1,end):
        if(array[j]<array[min_idx]):
              min_idx=j
      array[i],array[min_idx]=array[min_idx],array[i]
   
if __name__=="__main__":
   
    Arraysize=30000
    ObtainedArray=RandomArray(Arraysize)
    start_time=time.time()
    SelectionSort(ObtainedArray,0,Arraysize)
    end_time=time.time()
    runtime=end_time-start_time
    print("Runtime of SelectionSort is ",runtime," seconds")

    with open('SortedSelectionSort.csv','w',newline='') as file:
        writer=csv.writer(file)
        for i in ObtainedArray:
            writer.writerow([i])

    print("Sorted array saved to SortedSelectionSort.csv")         
            