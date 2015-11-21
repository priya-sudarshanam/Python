import Queue, Stack
import math
import CodingInterview
from CodingInterview import *
from Stack import *

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

    def getData(self):
        return self.data

    def setData(self,data):
        self.data = data

    def setNext(self,data):
        self.next = data

    def getNext(self):
        return self.next
    
class OrderedList:
    def __init__(self):
        self.head = None
        
    def isEmpty(self):
        return self.head == None

    def printMyList(self):
        current = self.head
        while current != None:
            print current.data
            current = current.getNext()

    def search(self, data):
        curr = self.head
        found = False
        stop = False
        while curr != None and not found and not stop:
            if curr.getData() == data:
                found = True
                stop = True
            elif curr.data < data:
                stop = True
            else:
                curr = curr.getNext()
        return found


    def add(self,data):
        temp = Node(data)
        current = self.head
        prev = None
        stop = False
        while current != None and not stop:
            if current.getData() > temp.getData():
                stop = True
            else:
                prev = current
                current = current.getNext()

        if prev == None:
            temp.setNext(current)
            self.head = temp
        elif current == None:
            temp.setNext(None)
            prev.setNext(temp)
        else:
            temp.setNext(current)
            prev.setNext(temp)
      
class UnorderedList:
    def __init__(self):
         self.head = None

    def isEmpty(self):
        return self.head == None

    def add(self,data):
        temp = Node(data)
        temp.setNext(self.head)
        self.head = temp

    def size(self):
        current = self.head
        ctr = 0
        while current != None:
            ctr += 1
            current = current.getNext()

        print ctr

    def search(self,data):
        current = self.head
        found = False
        ctr = 0
        while not found or current!= None:            
            if current.data == data:
                found = True
            ctr += 1
            current = current.getNext()
        return found

    def printMyList(self):
        current = self.head
        while current != None:
            print current.data
            current = current.getNext()
            
    def remove(self,data):
        current = self.head
        temp = None
        found = False
        while not found:
            if current.data == data:
                found = True
            else:
                temp = current
                current = current.getNext()

        if found:
            print "data is" ,data
            if temp == None:
                self.head = current.getNext()
            elif current.getNext() == None:
                temp.setNext(None)
            else:
                temp.setNext(current.getNext())


class NodeDLL:
    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None

    def getData(self):
        return self.data

    def setData(self,newData):
        self.data = newData        

    def getNext(self):
        return self.next

    def getPrev(self):
        return self.prev

    def setNext(self, newData):
        self.next = newData

    def setPrev(self,newData):
        self.prev = newData


###########################################################
# DoubleLinkedList

class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def isEmpty(self):
        return self.head == None

    def size(self):
        current = self.head
        ctr = 0
        while current <> None:
            ctr == 1
            current = current.getNext()

        return ctr

    def add(self,item):
        newItem = NodeDLL(item)
        if self.head is None:
            self.head = newItem
            newItem.setNext(self.tail)
        else:
            self.head.prev = newItem
            newItem.setNext(self.head)
            self.head = newItem
        
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

    def insertItemAtTail(self,item):
        newItem = NodeDLL(item)
        current = self.head
        while current.getNext() <> None:
            current = current.getNext()

        newItem.setNext(self.tail)
        newItem.setPrev = current
        current.setNext(newItem)
        
    def delHead(self):
        current = self.head
        temp = current.getNext()
        self.head = temp

    def printDLL(self):
        current = self.head
        while current <> None:
            print current.data
            current = current.getNext()

    def middleElt(self):
       
        current = self.head
        prev = self.head
        midElt = None
        ctr = 0
        while current <> None and current.getNext() <> None:
            ctr += 1
            current = current.getNext().getNext()
            prev = prev.getNext()
            
        return "index is %s, element is %s " %(ctr,prev.data)             
            
    def delTail(self):
        current = self.head
        prev = None
        while current.next <> None:
            prev = current
            current = current.getNext()
        
        prev.setNext(self.tail)

                
class Node:
    def __init__(self,data,left = None,right = None,parent=None):
        self.data = data
        self.left = left
        self.right = right
        self.parent = parent
        

class BinaryTree:
    def __init__(self):
        self.root = None

    def add(self,data):
        return Node(data)
        
    def insert(self,root,data,parent = None):
        if root:
            if root.data <= data:
                root.right = self.insert(root.right,data,root)
            else:
                root.left = self.insert(root.left,data,root)
            return root
        else:
             return self.add(data)

    def inOrder(self,root):
         if root:
             self.inOrder(root.left)
             print root.data,
             self.inOrder(root.right)

    def revOrder(self,root):
        if root:
            self.revOrder(root.right)
            print root.data,
            self.revOrder(root.left)

    def preOrder(self,root):
        if root:
            print root.data,
            self.preOrder(root.left)
            self.preOrder(root.right)

    def postOrder(self,root):
        if root:
            self.preOrder(root.left)
            self.preOrder(root.right)
            print root.data,

    def search(self,root,data):
        found = False
        stop = False
        while not stop and not found:
          if root:
            if root.data == data:
                found = True
                stop = True
            elif root.data < data:
                return self.search(root.right,data)
            elif root.data > data:
                return self.search(root.left,data)
            else:
                found = False
                stop = True

        return found
        

    def getMin(self, root):        
        if root:
            while root.left:
                root = root.left
        return root.data

    def getMaxLeftTree(self,root):
        if root:
            while root.left:
                root = root.left.right
        return root.data

    def getMinRightTree(self,root):
        if root:
            while root.right:
                root = root.right.left
        return root.data 
        
    def getMax(self, root):        
        if root:
            while root.right:
                root = root.right
        return root.data

    def getHeight(self,root):
        if not root:
            return 0
        else:
            l = self.getHeight(root.left)
            r = self.getHeight(root.right)
            return max(l,r) + 1

    def getBalanced(self,root):
        balanced = False
        if not root:
            balanced = True
        l = self.getHeight(root.left)
        r = self.getHeight(root.right)
        if 0 <= abs(l-r) <= 1:
           balanced = True
        return balanced       


    def size(self,root):
        if not root:
            return 0
        return 1 + self.size(root.left) + self.size(root.right)

    def convertArray(self,root):
        if not root:
            return []
        return [root.data] + self.convertArray(root.left) + \
               self.convertArray(root.right)

    def predSucc(self,root,node):
        pred,succ = 0,0
        if root and self.search(root,node):
            l = sorted(self.convertArray(root))
            dataIndex = l.index(node)
            pred = l[dataIndex-1]
            succ = l[dataIndex+1]
        return pred,succ
                
    def succTree(self,root,node):
        current = root
        succ = None
        
        if not root:
            return succ
        
        while current.data != node:
               if current.data > node:
                   succ = current
                   current = current.left
               else:
                   current = current.right           
            
        if current and current.right:
           succ = self.getMin(current.right) 

        if succ:
            return succ.data
        else:
            return None

    def predTree(self,root,node):
        current = root
        pred = None
        if not root:
            return pred
        while current.data != node and current:
               if current.data > node:
                   current = current.left
               else:
                   pred = current
                   current = current.right            
            
        if current and current.left:
           succ = self.getMax(current.left) 
                 
        if pred:
            return pred.data
        else:
            None

    def childrenCount(self,root,node):
        ct = 0
        if root:
            if root.data == node:
                if root.left and root.right:
                    ct += 2
                elif root.left or root.right:
                    ct += 1
            elif root.data < node:
                return self.childrenCount(root.right,node)
            else: 
                return self.childrenCount(root.left,node)
            
        return ct

    def compareTrees(self,root1,root2):
        treeEqual = True
        if not root1 and root2:
            return "missing roots: ",treeEqual
            return
        else:
            while not treeEqual and root1 and root2: 
                if root1.data <> root2.data:
                  treeEqual  = False
                  
                root1 = root1.left
                root2 = root2.left

            while root1 and root2:
                if root1.data <> root2.data:
                  treeEqual  = False                  
                root1 = root1.right
                root2 = root2.right
           
                     
        return "roots are :", "Equal" if treeEqual else "UnEqual"

    def delNode(self,root,item):
        delNode = False
        current = root
        found = False
        prev = None
        stop = False
        while not found and not stop and current:
            if current.data == item:
                found = True
                stop = True            
            else:
                prev = current
                if current.data > item:
                  current = current.left
                else:
                  current = current.right

        if found:           
           if current.left == None and current.right == None:               
               if prev.right == current:
                   prev.right = None                   
               else:
                   prev.left = None
           elif current.left and not current.right:              
               if prev.right == current:
                   prev.right = current.left                   
               else:
                   prev.left = current.left
           elif current.right and not current.left:
                if prev.right == current:
                   prev.right = current.right                   
                else:
                   prev.left = current.right
           else:
               prev = current
               succ = current.right
               while succ.left:
                   current = succ
                   succ = succ.left
               prev.data = succ.data 
               if current.left == succ:
                   current.left = succ.right
               else:
                   current.right = succ.right                   
                    

class SetOfStacks():
    def __init__(self,capacity):
        self.capacity = capacity
        self.stacks = []

    def push(self,item):
        if (len(self.stacks) == 0) or \
           (len(self.stacks[-1]) == self.capacity):
            self.stacks.append([])
        self.stacks[-1].append(item)

    
    def pop(self):
        if len(self.stacks) == 0:
            return None
        data = self.stacks[-1].pop()
        if len(self.stacks[-1]) == 0:
            self.stacks.pop()

    def popAt(self,index):
        if index < 1 or index > len(self.stakcs) or \
           len(self.stacks[-1]) == 0:
            return None
        else:
            return self.stacks[index-1].pop()


class SingleArrayStacks():
    def __init__(self,stacksize=100,number=3):
        self.ss = stacksize
        self.number = number
        self.array = [None]*stacksize*number
        self.pointer = -1 * self.number

    def stacktop(self,stacknum):
        return self.ss * stacknum + self.pointer[stacknum]

    def push(self,stacknum,value):
        if self.pointer[stacknum] + 1 > self.ss:
            print "out of space"
        else:
            self.pointer[stacknum] += 1
            self.array[self.stacktop(stacknum)] = value

    def pop(self,stacknum):
        if self.pointer[stacknum] < 0:
            print "Empty stack"
        else:
            data = self.array[self.stacktop(stacknum)]
            self.array[self.stacktop(stacknum)] = None
            self.pointer[stacknum] -= 1
            return data

    def peek(self,stacknum):
        if self.pointer[stacknum] < 0:
            return "Empty stack"
        else:
            return self.array[self.stacktop(stacknum)]
    

def binarySearch(alist,item):
  low = 0
  hi = len(alist) - 1
  found = False
  while low <= hi and not found:
    mid = (low + hi) // 2
    if alist[mid] == item:
      found = True
      return found, alist.index(item)
    else:
       if alist[mid] > item:
          hi = mid - 1
       else:
          low = mid + 1

          

