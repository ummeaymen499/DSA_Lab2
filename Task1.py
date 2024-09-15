import random

def RandomArray(size):
    Array=[]
    for i in range(size):
        num=random.randint(0,20)
        Array.append(num)
    return Array    
if __name__=="__main__":
   Size=input("Enter Size of the array: ")
   ArraySize=int(Size)
   ReqArray=RandomArray(ArraySize)
   print(ReqArray)