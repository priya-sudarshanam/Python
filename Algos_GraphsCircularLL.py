import Graphs
from Graphs import *
from pythonds.basic import Queue

#############################################################3
def bfs(g,start):
   visited, queue = [],[start]
   while queue:
       vertex = queue.pop(0)
       if vertex not in visited:
           visited.append(vertex)
           queue.extend(g[vertex] - set(visited))
   return visited


def dfs(g,start):
   visited, stack = [],[start]
   while stack:
       vertex = stack.pop()
       if vertex not in visited:
           visited.append(vertex)
           stack.extend(set(g[vertex]) - set(visited))
   return visited


def pathToGoalYield(graph, start, goal):
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        for next in graph[vertex] - set(path):
          if next == goal:
              yield path + [next]
          else:
              queue.append((next, path + [next]))

def pathToGoalRef(graph, start, goal, path=None):
    if path is None:
        path = [start]
    if start == goal:
        if not path == None:
            print path
    for next in graph[start]-set(path):
        if not pathToGoalRef(graph,next,goal,path +[next]) == None:
            print pathToGoalRef(graph,next,goal,path +[next])


# without yield
def pathToGoal(graph, start, goal):
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        for next in graph[vertex]-set(path):
            if next == goal:
                temp =  path + [next]
                pathToGoal(graph,next,goal)
                print temp                                
            else:
                stack.append((next, path + [next]))
def shortestPath(graph,start,goal):
    try:
        return next(pathToGoalYield(graph,start,goal))
    except StopIteration:
        return None


def dfs(graph, start):
    visited, stack = [], [start]
    while stack:
       vertex = stack.pop()       
       if not vertex in visited:
            visited.append(vertex)
            stack.extend(set(graph[vertex]) - set(visited))
    return visited

def dfs(graph, start, visited=None):
    if visited is None:
        visited = []
    visited.append(start)
    for a in graph[start]:
        if a not in visited:
          dfs(graph,a,visited)
    return visited

#################################################################
#Binary Search Tree

class Node:
    def __init__(self,data,left=None,right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return "(" + str(self.data) + "(" + str(self.left) + " |" + str(self.right) + "))"
    

class BTree:
    def __init__(self):
        self.root = None
        
    def addNode(self,data):
        return Node(data)

    def insert(self, root, data):
        if root:
           if data <= root.data:
                root.left = self.insert(root.left, data)
           else:
                root.right = self.insert(root.right, data)
           return root
        else:
           return self.addNode(data)
     
    def lookup(self, root, target, parent=None):
        found = False
        if root:
          if target == root.data:
              found = True
          elif target < root.data:
             return self.lookup(root.left, target, root)
          else:
             return self.lookup(root.right, target,root)
        else:
          found = False

        if parent:
            return found,parent,parent.data,target
        elif not root or not parent:
            return found,None,None,target
        
    def getMin(self,root):
        if root:
          while root.left:
              root = root.left
              
        return root.data

    def getMax(self,root):
        if root:
          while root.right:
              root = root.right
              
        return root.data

    def treeHeight(self,root):
        if root == None:
          return 0
        else:
            l = self.treeHeight(root.left)
            r = self.treeHeight(root.right)
            return max(l,r) + 1

    def isBalanced(self,root):
        balanced = False
        if root == None:
          return 0
        else:
            l = self.treeHeight(root.left)
            r = self.treeHeight(root.right)
            if 0 >= abs(l - r) <= 1:
                balanced = True
            
        return balanced
        
    def childrenCount(self, root,node):
        cnt = 0
        f,p,pdata,d = self.lookup(root,node)
        if f:
          if d == root.data:
            if root.left:
                  cnt += 1
            if root.right:
                  cnt += 1
          elif node < root.data:
            return self.childrenCount(root.left, node)
          else:
            return self.childrenCount(root.right, node)
        else:
            cnt = -1
        
        return cnt

    def inOrder(self,root):
        if root:
          self.inOrder(root.left)
          print root.data,
          self.inOrder(root.right)

    def postOrder(self,root):
        if root:
          self.postOrder(root.left)
          self.postOrder(root.right)
          print root.data,

    def preOrder(self,root):
        if root:
          print root.data,
          self.preOrder(root.left)
          self.preOrder(root.right)          

    def revOrder(self,root):
        if root:
          self.revOrder(root.right)
          print root.data,
          self.revOrder(root.left)

    def size(self,root):
        if root:
            return (self.size(root.left) + 1 + self.size(root.right))
        else:
            return 0

    def convertArray(self,root):
        if not root:
          return []
        return [root.data] + self.convertArray(root.left) + self.convertArray(root.right)

    def returnPreAndSuc(self,root,node):
            #way 1
            if root and self.lookup(root,node):
                l = sorted(self.convertArray(root))
                m = l.index(node)
                predeccesor = l[m-1]
                successor = l[m+1]
            return "Predecessor and Successor: %s, %s"%(predeccesor,successor)

    def compareTrees(self,root1,root2):
        # way 1
##        r1 = self.convertArray(root1)
##        r2 = self.convertArray(root2)
##        treeSame = False
##        if root1 and root2 and (root1 == root2):
##          treeEqual = [i for i, j in zip(r1, r2) if i <> j]
##        
##        if not treeEqual:
##           treeSame = True
##        return treeSame
        
        #way 2
        treeEqual = False
        if not root1 and root2:
            return "missing roots: ",treeEqual
            return            
        else:
            if root1.data <> root2.data:
              return "roots are unequal: ",treeEqual
              return
            else:
              while root1.left and root2.left:
                if root1.left.data <> root2.left.data:
                    return "left side of tree unequal: ",treeEqual 
                    return
                return self.compareTrees(root1.left,root2.left)
                                                        
              while root1.right and root2.right:
                if root1.right.data <> root2.right.data:
                    return "right side of tree unequal: ",treeEqual
                    break
                return self.compareTrees(root1.right,root2.right)
            
        treeEqual = True           
        return treeEqual         

    def deleteNode(self,root,node):
        if root:
            f,p,pdata,t = self.lookup(root,node)
            if f:
              if self.childrenCount(root,t) == 0:
                 if p.right is t:
                    p.right = None
                 else:
                    p.left = None
              elif self.childrenCount(root,t) == 1:
                   if p.right.data is t:
                       if p.right.right:
                         p.right = p.right.right
                       elif p.right.left:
                         p.right = p.right.left                      
                   else:
                      if p.left.right:
                        p.left = p.left.right
                      else:
                         p.left = p.left.left
              else:
                  successor = p.right
                  while successor.left:
                      p = successor
                      successor = successor.left
                  p.data = successor.data
                  if p.left == successor:
                      p.left = successor.right
                  else:
                      p.right = successor.right                     


def makeBalancedTree(l):
    if len(l) == 0:
        return None
    elif len(l) == 1:
        return Node(l)
    else:
        mid = len(l)/2
        return Node(l[mid],makeBalancedTree(l[:mid]),\
                    makeBalancedTree(l[mid+1:]))



#####################################################################
##BinHeap

class BinHeap:
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0

    def percUp(self,i):
        while i // 2 > 0:
          if self.heapList[i] < self.heapList[i // 2]:
             self.heapList[i // 2],self.heapList[i] = \
                self.heapList[i], self.heapList[i // 2]
             
          i //= 2

    def insert(self,k):
        self.heapList.append(k)
        self.currentSize += 1
        self.percUp(self.currentSize)
 
    def minChild(self,i):
        minVal = 0
        if ((i * 2) + 1) > self.currentSize:
           minVal =   i * 2
        else:
            if self.heapList[i*2] < self.heapList[i*2+1]:
                 minVal =  i * 2
            else:
                 minVal = i * 2 + 1
        return minVal

    def percDown(self,i):
        while (i*2) <= self.currentSize:
            mc = self.minChild(i)
            if self.heapList[i] > self.heapList[mc]:
                self.heapList[i], self.heapList[mc] = \
                    self.heapList[mc], self.heapList[i]
                
            i = mc

    def delMin(self):
        retval = self.heapList[1]
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize -= 1
        self.heapList.pop()
        self.percDown(1)
        return retval

    def buildHeap(self,alist):
        i = len(alist) // 2
        self.currentSize = len(alist)
        self.heapList = [0] + alist[:]
        while (i>0):
            self.percDown(i)
            i = i-1        
        
    def printHeap(self):
        print self.heapList


############################################################
        # Circular Linked List

class Node:
    def __init__(self,initData):
        self.data = initData
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self,newData):
        self.data = newData

    def setNext(self,newNext):
        self.next = newNext


class CircularList:
    def __init__(self):
        self.head = Node(None)
        self.head.setNext(self.head)

    def add(self,item):
        temp = Node(item)
        if self.head is None:
            temp.setNext(self.head)
            self.head.setNext(temp)
        else:
            current = self.head
            while current.getNext() <> self.head:
                  current = current.getNext()

            current.setNext(temp)
            temp.setNext(self.head)
            
    def addAfterHead(self,item):
        temp = Node(item)
        prev = self.head
        current = self.head.getNext()
        prev.setNext(temp)
        temp.setNext(current)

    def getCenterElt(self):
        slow = self.head
        fast = self.head
        ctr = 0
        while fast.getNext() <> self.head or fast.getNext().getNext() <> self.head:
            ctr += 1
            slow = slow.getNext()
            fast = fast.getNext().getNext()

        centerStr = "Middle of the list is: %s and index position is: %s"\
                    %(slow.getData(),ctr)
        
        return centerStr

    def printList(self):
        current = self.head.getNext()
        ctr = 0        
        while current <> self.head:            
            ctr += 1
            print "Element at position %s is: %s"%(ctr,current.getData())
            current = current.getNext()

        printStr = "size of the list is: ", ctr
        
        return printStr

    def index(self, item):
        current = self.head.getNext()
        ctr = 0
        found = False
        while not found and current <> self.head:
            ctr += 1
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()

        if not found:
            ctr = -1

        if ctr > 0:
            return "found and index is: {0}", ctr
        else:
            return "not found"

    def removeHead(self):
        current = self.head.getNext()
        prev = self.head.getNext()
        while current.getNext() <> self.head:
            current = current.getNext()

        self.head = prev
        current.setNext(self.head)
 
    def pop(self):
        current = self.head.getNext()
        prev = None
        while current.next <> self.head:
            prev = current
            current = current.getNext()

        prev.setNext(self.head)
        
    def isCircular(self):
        circular = False
        slow = self.head
        fast = slow.getNext()
        while fast.getNext() <> None:
          if (fast == slow or fast.getNext() == slow):
                circular = True                
                break
          else:
                slow = slow.getNext()
                fast = fast.getNext().getNext()
                
        return circular,slow.getData()  

###########################################################
#Graphs



############################################################
#Tests


#####################Graph testing
g = Graph()

for i in ['A','B','C','D','E','F']:
    g.addVertex(i)


g = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}
for v in g:
    for i in v.getConnections():
        print("( %s , %s )" % (v.getId(), i.getId()))


#########################################################
#Tree tests

##l = [1,2,3,4,5,6,7,8,9,10,12]
##print makeBalancedTree(l)
    
##if __name__ == "__main__":
##    bTree = BTree()
##    root = bTree.addNode(7)
##  #  root1 = bTree.addNode(8)
##    for i in range(0, 12):
##        data = int(raw_input("insert the node value for tree1 %d: " % i))
##        bTree.insert(root, data)
##    print
##
##    print "Tree balanced: ",bTree.isBalanced(root)
####    for i in range(0, 4):
##        data = int(raw_input("insert the node value for tree2 %d: " % i))
##        bTree.insert(root1, data)
##    print    

##    data = int(raw_input("insert a value to find: "))
##    f,p,t = bTree.lookup(root, data,None)
##    if f:
##       print "parent,target: %s,%d" %(p,t)
##    else:
##       print "not found"

##    print "Minimum of the tree is: ", bTree.getMin(root)
##    print "Maximum of the tree is: ", bTree.getMax(root)
##    print "Height of the Tree is: ", bTree.treeHeight(root)
    #cdata = int(raw_input("insert node to find children: "))
    #ctr = bTree.childrenCount(root,cdata)
    #print ctr
    #if ctr >= 0:
     #   print "Number of children for node: %s is : %s " %(cdata,ctr)
    #else:
     #   print "Node %s has no children" %(cdata)    


   # print "Inorder Traversal: \n", bTree.inOrder(root)
##    print "Preorder Traversal: \n", bTree.preOrder(root)
##    print "Postorder Traversal: \n", bTree.postOrder(root)
##    print "Reverse Order: \n", bTree.revOrder(root)
##    print "\nSize of the tree is: ", bTree.size(root)
   # bTree.compareTrees(root,root1)
    #node = int(raw_input("insert the node for deleting : "))    
    #print bTree.returnPreAndSuc(root,node)
    #bTree.deleteNode(root,node)
    #print "Inorder Traversal: \n", bTree.inOrder(root)
               


###########################################################
#BinHeap
bh = BinHeap()
##bh.insert(5)
##bh.insert(9)
##bh.insert(11)
##bh.insert(14)
##bh.insert(18)
##bh.insert(19)
##bh.insert(21)
##bh.insert(33)
##bh.insert(17)
##bh.insert(27)
###print bh.minChild(2)
##bh.printHeap()
##bh.delMin()
##bh.printHeap()

alist= [9, 6, 5, 2, 3]
bh.buildHeap(alist)
bh.printHeap()


#############################################################
#Circular Linked List

myList = CircularList()
myList.add(16)
myList.add(31)
myList.add(64)
myList.add(34)
print myList.printList()
myList.addAfterHead(17)
#print myList.pop()
#print myList.index(34)
#print myList.pop()
#print myList.removeHead()
print myList.printList()
#print myList.getCenterElt()
print myList.isCircular()

