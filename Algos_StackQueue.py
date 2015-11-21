class Hashtable:
    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def hashFunction(self,key,size):
        return key%size

    def rehash(self,oldHash,size):
        return (oldHash+1)%size


    def put(self,key,data):
        hashValue = self.hashFunction(key,len(self.slots))

        if self.slots[hashValue] == None:
            self.slots[hashValue] = key
            self.data[hashValue] = data
            
        else:
            if self.slots[hashValue] == key:
                self.data[hashValue] = data
            else:
                nextSlot = self.rehash(hashValue,len(self.slots))
                while self.slots[nextSlot] != None and self.slots[nextSlot] != key:
                    nextSlot = self.rehash(nextSlot,len(self.slots))

                
                if self.slots[nextSlot] == None:
                    self.slots[nextSlot] = key
                    self.data[nextSlot] = data
            
                else:
                    self.data[nextSlot] = data


    def get(self,key):
          startSlot = self.hashFunction(key,len(self.slots))
          found = False
          stop = False
          position = startSlot
          data = None

          while self.slots[position] != None and not found and not stop:
              if self.slots[position] == key:
                  data = self.data[position]
                  found = True
                  stop = True
              else:
                  position = self.rehash(position,len(self.slots))
                  if self.slots[position] == startSlot:
                      stop = True

          return data

    def __getitem__(self,key):
        return self.get(key)

    def __setitem__(self,key,data):
        return self.put(key,data)

###########################################################
##Deque

class Deque:
    def __init__(self):
        self.items=[]

    def isEmpty(self):
        return self.items == []

    def addFront(self,item):
        self.items.append(item)

    def addRear(self,item):
        self.items.insert(0,item)

    def removeFront(self):
        return self.items.pop()

    def removeRear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)

    def dPrint(self):
        for i in self.items:
            print i


#############################################################
#Stack

class Stack:
    def __init__(self):
        self.items = []
        self.minItems = []

    def isEmpty(self):
        return self.items == []

    def push(self,item):
        self.items.append(item)

    def pop(self):
      if not self.isEmpty():
         return self.items.pop()

##    def minStack(self):
##        return self.orderDesc()

    def peek(self):
        if not self.isEmpty():
          return self.items[len(self.items) - 1]
        #else:
         #return 0

##    def size(self):
##        return len(self.items)
##
##    def printStack(self):
##        for i in self.items:
##            print i
##        
##    def orderAsc(self):
##        m = Stack()
##        temp = Stack()
##        while self.size() > 0:
##              if not m or self.peek() > m.peek():
##                m.push(self.pop())
##              else:
##                  while m.size()>0:
##                    temp.push(m.pop())
##                  m.push(self.pop())
##
##        while temp.size() > 0:          
##            m.push(temp.pop())
##            
##        m.printStack()
##
##    def orderDesc(self):
##        temp = Stack()
##        while self.size() > 0:
##            if not self.minItems or self.peek() > self.minItems[0]:
##                self.minItems.append(self.pop())
##            else:
##                self.minItems.insert(0,self.pop())
##        return self.minItems[0]
##                


##############################################################
#Min Stack

class Stack:
    def __init__(self):
        self.items = []
        self.min = []

    def isEmpty():
        return self.items == []
    
    def push(self,item):
        self.items.append(item)
        if not self.min or item <= self.minStack():
            self.min.append(item)         
        
    def pop(self):
        if not self.isEmpty():
           return self.items.pop()

    def minStack(self):
       return self.min[-1]
                

################################################################
#Queue

class TestQueue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        if not self.isEmpty():
           return self.items.pop()
        else:
           return "queue is empty"

    def size(self):        
        return len(self.items)

    def minQueue(self, itemLst):
        minQ = sys.maxint
        for i in range(len(itemLst)):
            if i < minQ:
                minQ = i
                self.enqueue(i)
            else:
                temp = self.dequeue()
                self.enqueue(minQ)


################################################################
#deque

class Deque:
    def __init__(self):
        self.list = []

    def isEmpty(self):
        return self.list == []

    def addRear(self,item):
        self.list.insert(0,item)

    def addFront(self,item):
        self.list.append(item)

    def removeRear(self):
        return self.list.pop(0)

    def removeFront(self):
        return self.list.pop()

    def size(self):
        return len(self.list)

############################################################
#Unordered List

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

    def getData(self):
        return self.data

    def setData(self,data):
        self.data = data

    def getNext(self):
        return self.next

    def setNext(self,data):
        self.next = data
       

class UnorderedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def printList(self):
        current = self.head
        while current <> None:
            print current.data
            current = current.getNext()

    def add(self,item):
        newNode = Node(item)
        newNode.setNext(self.head)
        self.head = newNode

    def search(self,item):
        current = self.head
        found= False
        ctr = 0
        while not found and current.getNext <> None:
            ctr += 1
            if current.data == item:
                 found = True
            current = current.getNext()
        return ctr,found

    def size(self):
        current= self.head
        ctr = 0
        while current <> None:
            ctr += 1
            current = current.getNext()
        return ctr
        
    def middleElt(self):
        current = self.head
        prev = self.head
        midElt = None
        ctr = 0
        while current.getNext() or current.getNext().getNext() != None:
            ctr += 1
            prev = prev.getNext()
            current = current.getNext().getNext()

        return ctr,prev.data

    def revList(self):
        current = self.head
        prev = None
        while current <> None:
            temp = current.getNext()
            current.setNext(prev)
            prev = current
            current = temp

        self.head = prev
        while prev <> None:
            print prev.getData()
            prev = prev.getNext()
        return

    def remove(self,item):
        current = self.head
        stop = False
        prev = None
        if self.search(item)[1]:
          while not stop:
              if current.getData() == item:
                    stop = True
              else:
                  prev = current
                  current = current.getNext()

          if stop:
            if prev == None:
               self.head = current.getNext()
            elif current.getNext() == None:
               prev.setNext(None)
            else:
                prev.setNext(current.getNext())
               


###############################################################
##Tests
    
H = Hashtable()
H[54] = "cat"
H[26]="dog"
H[93]="lion"          
H[17]="tiger"
H[77]="bird"
H[31]="cow"
H[44]="goat"
H[55]="pig"
H[20]="chicken"
H[25]="elephant"
H[20]="cheetah"
print H[20]
print H[99]


