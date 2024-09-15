from Task1 import RandomArray
import time
import csv
def BubbleSort(array,start,end):
    for i in range(start,end):
        for j in range(start,end-i-1):
            if(array[j]>array[j+1]):
                array[j],array[j+1]=array[j+1],array[j]
if __name__=="__main__":
   
    Arraysize=30000
    ObtainedArray=RandomArray(Arraysize)
    start_time=time.time()
    BubbleSort(ObtainedArray,0,Arraysize)
    end_time=time.time()
    runtime=end_time-start_time
    print("Runtime of BubbleSort is ",runtime," seconds")

    with open("SortedBubbleSort","w",newline="") as file:
        writer=csv.writer(file)
        for number in ObtainedArray:
            writer.writerow([number])

    print("Sorted array saved to SortedBubbleSort.csv")

    