import random
def BubbleSort(array,start,end):
    for i in range(start,end):
        for j in range(start,end-i-1):
            if(array[j]>array[j+1]):
                array[j],array[j+1]=array[j+1],array[j]

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
                            
def InsertionSort(array,start,end):
    for j in range(start+1,end):
        key=array[j]
        i=j-1
        while i>=start and array[i]>key:
            array[i+1]=array[i]
            i=i-1 
        array[i+1]=key

def MergeSort(array, start, end):
    if(end - start <= 1): 
        return array
    else:
        m = (start + end) // 2
        MergeSort(array, start, m)
        MergeSort(array, m, end)

        Merge(array, start, m, end)

def SelectionSort(array,start,end):
   for i in range(start,end-1):
      min_idx=i
      for j in range(i+1,end):
        if(array[j]<array[min_idx]):
              min_idx=j
      array[i],array[min_idx]=array[min_idx],array[i]

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

def RandomArray(size):
    Array=[]
    for i in range(size):
        num=random.randint(0,20)
        Array.append(num)
    return Array                                                        

def ShuffleArray(array, start, end):
  
    sub_array = array[start:end]  
    random.shuffle(sub_array)     
    array[start:end] = sub_array  
    return array