####Searching and Sorting
def seqSearch(alist,item):
    found = False
    j = 0
    for i in range(len(alist)):
        if alist[i] == item:
            found = True
            j = i
                            
    return found,j

def binSearch(alist,item):
    first  = 0
    end = len(alist) - 1
    found = False    
    while first <= end and not found:
        mid = (first + end) // 2
        if alist[mid] == item:
            found = True
        else:
            if alist[mid] > item:
                end = mid - 1
            else:
                first = mid + 1
    return found     
        

def selectSort(alist):    
    for i in range(len(alist)-1,0,-1):
        maxposn = 0
        for j in range(1,i+1):
            if alist[j] > alist[maxposn]:
                maxposn = j
                
        alist[i],alist[maxposn] = alist[maxposn],alist[i]
    return alist
             
def insertSort(alist):
    for i in range(1,len(alist)):
        currPos = i
        currVal = alist[i]
        while currPos > 0 and alist[currPos - 1] > currVal:
            alist[currPos] = alist[currPos-1]
            currPos = currPos-1
        alist[currPos] = currVal
    return alist


def mergeSort(alist):
   if len(alist) > 1:
       mid = len(alist) //2
       leftHalf = alist[:mid]
       rightHalf = alist[mid:]

       mergeSort(leftHalf)
       mergeSort(rightHalf)

       i,j,k = 0,0,0

       while i < len(leftHalf) and j < len(rightHalf):
           if leftHalf[i] < rightHalf[j]:
               alist[k] = leftHalf[i]
               i += 1
           else:
               alist[k] = rightHalf[j]
               j += 1
           k += 1
   
       while i< len(leftHalf):
           alist[k] = leftHalf[i]
           i += 1
           k += 1

       while j < len(rightHalf):
           alist[k] = rightHalf[j]
           j += 1
           k += 1
           
   return alist 
           
def quickSort(alist):
    quickSortHelper(alist,0,len(alist)-1)

def quickSortHelper(alist,first,last):
    if first < last:
        splitPoint = partition(alist,first,last)

        quickSortHelper(alist,first,splitPoint-1)
        quickSortHelper(alist,splitPoint+1,last)        

def partition(alist,first,last):
    pivot = alist[first]
    leftMark = first + 1
    rightMark = last

    done = False

    while not done:
        while leftMark <= rightMark and alist[leftMark] <= pivot:
            leftMark += 1

        while alist[rightMark] >= pivot and rightMark >= leftMark:                          
            rightMark -= 1

        if rightMark < leftMark:
            done = True
        else:
            alist[leftMark],alist[rightMark] = alist[rightMark],alist[leftMark]

    alist[first],alist[rightMark] = alist[rightMark],alist[first]

    return rightMark
