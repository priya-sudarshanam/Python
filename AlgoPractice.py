##import re, unittest, Stack, TestQueue
##from Stack import *
##from TestQueue import *
##


def addNum(lst,lst2):
    str1, str2 = "", ""   
    for i,j in  zip(lst,lst2):
      str1 += str(i)
      str2 += str(j)
    
    sumNum = int(revStr(str1)) + int(revStr(str2))
    myList = UnorderedList()
    for i in str(sumNum):
        myList.add(i)

    myList.printList()
  #  print sumNum


def kthToLast(l, k):
    if k <= 0:
        return "invalid k"
    lenl = l.size()
    elt = lenl - k
    ctr = 0
    current = l.head
    while ctr < elt:
        ctr += 1
        current = current.next

    return current.data
def postfixEval(s):
    opS = Stack()
    tokenList = s.split()
    for token in tokenList:
        if token in "0123456789":
            opS.push(token)
        else:
            op1 = opS.pop()
            op2 = opS.pop()
            opS.push(calc(token,int(op1),int(op2)))
    return opS.pop()


def calc(op,op1,op2):
    if op == '/':
        return float(op1 / op2)
    elif op == '*':
        return op1 * op2
    elif op == '+':
        return op1 + op2
    elif op == '-':
        return op1 - op2


def infixToPostfix(s):
    prec = {}
    prec['/'] = 3
    prec['*'] = 3
    prec['-'] = 2
    prec['+'] = 2
    prec['('] = 1
    prec['^'] = 1

    alphaNumString = "ABCDEFGHIJKLMNOPQRSTUVWXYZ01234567891016"
    opS = Stack()
    operandList = []
    tokenList = s.split()

    for token in tokenList:
        if token in alphaNumString:
            operandList.append(token)
        elif token in "(":
            opS.push(token)
        elif token in ")":
            popToken = opS.pop()
            while popToken != "(":
                operandList.append(popToken)
                popToken = opS.pop()
        else:
            while (not opS.isEmpty()) and \
               (prec[opS.peek()] >= prec[token]):
                   operandList.append(opS.pop())
            opS.push(token)
  
    while not opS.isEmpty():
        operandList.append(opS.pop())
    print ' '.join(operandList)

def hotPotato(namelist,num):
    hQueue = Queue.Queue()
    for i in namelist:
        hQueue.put(i)

    while hQueue.qsize() > 1:
        for i in range(num):
            hQueue.put(hQueue.get())

        hQueue.get()

def decToBinary(n):
    s = Stack()
    q=0
    div = 2
    even = [0,2,4,6,8]
    m= n
    a = ""
    x = ""
    k = "-0b"
    if n == 0:
      print 0    
    else:
      if n <0:
        n = abs(n)
      while not n/div == q:        
        if int(str(n)[-1]) in even:
            s.push(0)
        else:
            s.push(1)
        q = n >> 1
        n = q       
    while not s.isEmpty():
        x += str(s.pop())
        
    if m < 0:
       a = k + x + "\n"
    else:
       a = x +"\n"
    return a


def paranChecking(paranString):
     s = Stack()   
     balanced = True
     opening = ["(","[","{"]
     matching = ["()","[]","{}"]
     output = "balanced"
     index = 0
     while index < len(paranString):
       for i in paranString:
        curr = paranString[index]
       if i in opening:
           s.push(i)                                 
       else:
           if s.isEmpty() or (s.pop()+i not in matching):
               balanced = False
            else:
               x = s.pop()               
               if x+curr not in matching:                   
                   balanced = False
                   return
                   
      index += 1
     return "unbalanced" if not (balanced and s.isEmpty()) else "balanced"


def permut1(s):
    res = []
    if len(s) == 1:
        res = [s]
    else:
        for i,c in enumerate(s):
            for j in permut1(s[:i]+s[i+1:]):
                res += [c + j]
    return res

def swapNumber(a,b):
    a,b = a + b - a, b + a - b
    return a,b
    
def contSum(l):
    maxS = 0
    suml = 0
    start, end, sum_start = -1, -1, -1
    m = []
    for i in l:
        suml += i
        if maxS < suml:            
            maxS = suml
            start,end = sum_start,l.index(i)
        elif suml < 0:
            suml = 0
            sum_start = l.index(i)
 
    return maxS,l[start+1: end+1]

def sortedAB(a,b):
    for i,j in zip(a,b):
        if j < i:
            m = a.index(i)
            a = a[:m] + [j] + a[m:]
    return a

def sortedAnag(a):
    a= sorted(a)
    for i in a:
      for j in a[a.index(i)+1:]:
        if anagramQueue(i,j):
            m = a.index(i)
            p = a.pop(a.index(j))
            a = a[:m] + [p] +a[m:]
    return a

def isDiv(n):
    evens = [2,4,6,8]
    odds = [3,6,9]
    nStr = str(n)
    factors = []
    x = isDiv3(n)
    if nStr[-1] == 0:
        factors.append(2)
        factors.append(5)
        factors.append(10)
    if int(nStr[-1]) in evens:
        factors.append(2)
        
    if len(str(x)) > 1:
        x = isDiv3(x)

    if x in odds:
         factors.append(3)
    
    if int(nStr[-1]) in [5]:
        factors.append(5)
    if 2 and 3 in factors:
        factors.append(6)    
        
    return factors
    
def factors(n):
    l = []
    l.append(1)
    
    if isDiv(n):
        fact = isDiv(n)
        print fact
        for i in fact:
            l.append(i)
    
    for i in range(7,int(math.floor(n/2)) + 1):
        if n % i == 0 and i not in l:
            l.append(i)
    
    l.append(n)
    return l

def changes(amount, coins):
    ways = [0] * (amount + 1)
    ways[0] = 1
    for coin in coins:
        for j in xrange(coin, amount + 1):
           ways[j] += ways[j - coin]
                       
    return ways



def secondLargest(l):
    fM,sM = l[0],l[1]    
    if fM < sM:
        fM, sM = l[1],l[0]
        
    for i in l[2:]:
        if i > fM:
            fM,sM = i,fM                       
    return fM,sM

  
def coinChange(amt,d):
    l = [0 for i in range(amt+1)]
    xl = [0 for i in range(amt+1)]
    l[0] = 0
    first, second = 0,0
    for i in range(1,amt+1):
        temp = float('inf')
        for j in (c for c in d if i >= c):
            temp = min(l[i-j],temp)
            if (l[i-j] == temp):
                xl[i] = j
            l[i] = temp + 1
    for i in xl:
        first = xl[amt]
        second = xl[first]
        
    print "Minimum Number of coins to get change: ",l[amt]
    print "\n The denominations are : (a) %d (b) %d " %(first,second)
    

  
def isSorted(s):
    i = 0
    j = len(s)
    k = math.ceil(len(s)/2)
    if len(s) > 2:
        while i <= k  and j >= k :
            if i == 0:
                if not s[i] < s[i+1]:
                    return "not sorted"
                    break
            elif j == -1:
                if not s[j] > s[j-1]:
                    return "not sorted"
                    break
            else:
                if not s[i-1] < s[i] < s[i+1] or \
                    not s[j-1] < s[j] < s[j+1]:
                    return "not sorted"
                    break
            i += 1
            j -= 1
        return "sorted"
    if len(s) == 2:
        if not s[0] < s[1]:
            return "not sorted"
            return

    return "sorted"

def factorial(n):
    if n < 0 or not isinstance(n, int):
        print "cannot give factorial of negative or float"
        os._exit(0)

    if n == 0:
      return 1
    else:
      return n * factorial(n-1)


def fibonacci(n):
    if n < 0 or not isinstance(n, int):
        print "cannot give fibonacci of negative or float"
        os._exit(0) 
    
    if n == 0:
     return 0
    elif n == 1:
     return 1
    else:
      return fibonacci(n-1) + fibonacci(n-2)

def balancedParan(st):
    s = Stack()
    balanced = True
    opening = ['(','{','[']
    full = ['()','[]','{}']
    for i in list(st):
       if i in opening:
           s.push(i)
       else:
          if s.isEmpty() or (s.pop() + i) not in full:
               balanced = False
    return balanced        

def decToBinary(n):
    s = Stack()
    q,r=0,0
    div = 2
    even = [0,2,4,6,8]
    if n == 0:
        return 0
    else:
      while n/div <> q:
         if int(str(n)[-1]) in even:
             s.push(0)
         else:
            s.push(1)

         q = n >> 1
         n = q

      while not s.isEmpty():
        print s.pop()

def compute(a,b,op):
    if op == '*':
        return a * b
    elif op == '+':
        return a + b
    elif op == '-':
        return a - b
    else:
        return float(a / b)

def evalExp(e):
    s = Stack()
    l = e.split()
    print l
    n = '0123456789'
    result = 0
    for i in l:
        if i in n:
            s.push(i)
        else:
            num1 = s.pop()
            num2 = s.pop()            
            result = compute(int(num1),int(num2),i)
            s.push(result)
    return s.pop()       
        

def palChecker(a):
    d = Deque()
    equal = True
    for i in a:
        d.addFront(i)

    while d.size() > 1 and equal:
        if d.removeFront() <> d.removeRear():
            equal = False
        
    return equal

def revString(a):
    s = Stack()
    for i in a:
        s.push(i)

    while s.size() > 0:
        print s.pop()
        
###Recursion
#####
def listSum(l):
    suml = 0
    if len(l) == 1:
        return l[0]
    else:
        return l[0]+listSum(l[1:])

           
def uniqChar(d):
    duplicate = False
    s = [False] * 26
    for i in range(len(d)):
        if d[i] in s:
            duplicate = True            
        s[i] = d[i]
    return duplicate
       
def revStr(s):
    rev = ""
    c = '\0'
    for i in s:
        rev = i + rev
    return c+rev

def revStrStack(d):
    s = Stack()
    c = '\0'
    x = ""
    for i in d:
        s.push(i)
        
    while not s.isEmpty():
        x += s.pop()
    return c+x

def anagram(a,b):
    dicta = {i:a.count(i) for i in a}
    dictb = {i:b.count(i) for i in b}
    isAnagram = False
    matched = len(set(dicta.items()) ^ set(dictb.items())) == 0
    if matched:
        isAnagram = True
    return isAnagram

def anagramQueue(a,b):
    x = sorted(a)
    y = sorted(b)
    qA = TestQueue()
    qB = TestQueue()
    anag = True    
    for i in x:
        qA.enqueue(i)
    for j in y:
        qB.enqueue(j)
    
    while not (qA.isEmpty() and qB.isEmpty()) and anag:
        if ((qA.isEmpty() and not qB.isEmpty()) or \
           (not qA.isEmpty and qB.isEmpty())):
            anag = False
        lA = qA.dequeue()
        lB = qB.dequeue()
        if lA <> lB:
            anag = False            
            
    return anag
   
def replaceSpace(d):
    return re.sub(r'\s','%20',d)

def isSubstring(a,b):
    return b in a

def isRotation(a,b):
    indexFirst = a.index(b[0])
    fullString = a+a
    return isSubstring(fullString,b)

def removeDuplicates(d):
    m = list(d)
    i = 0
    n = len(d)
    while i < n:
        if m[i] in m[i+1:]:
          del m[i]
          n -= 1
        else:
          i += 1
    return m

def matrixZero(m):
   zeroRow = []
   zeroCol = []
   for i, row in enumerate(m):
       for j, col in enumerate(row):
           if col is 0:
               zeroRow.append(i)
               zeroCol.append(j)

   for i, row in enumerate(m):
       for j, col in enumerate(m):
           if i in zeroRow or j in zeroCol:
               m[i][j] =0
   return m

def trailingZeros(n):
    ctr = 0
    for i in range(1,n+1):
        if str(i)[-1] in ['5','0']:
            ctr += 1
    return ctr

##    
####class codingInterviewTests(unittest.TestCase):
####    def testIsRotation(self):
####        self.assertTrue(isRotation("waterbottlewaterbottle","erbottlewat"))
####        self.assertFalse(anagram("hello","jake"))
####        self.assertEqual(removeDuplicates("hello"),['h', 'e', 'l', 'o'])
####        self.assertTrue(uniqChar("erbottlwa"))
####        self.assertFalse(uniqChar("erbotlwa"))
####        self.assertEqual(replaceSpace("h e l l o"),"h%20e%20l%20l%20o")
####        self.assertEqual(revStrStack("hello"), " olleh")

print paranChecking("(())") # balanced
print paranChecking("(()") #unbalanced
print paranChecking("(())]") #unbalanced
print paranChecking("{(())}") #balanced
print paranChecking("") #balanced
print paranChecking(" ") #unbalanced
print paranChecking("[(())}") #unbalanced
print paranChecking("{(}())") #unbalanced
print paranChecking("{()](())") #unbalanced

hotPotato(["Bill","David","Susan","Jane","Kent","Brad"],7)
infixToPostfix("( A + B ) * ( C + D )")
infixToPostfix("10 + 3 * 5 / ( 16 - 4 )")
infixToPostfix("( A + B ) * C")

print postfixEval('2 3 + 7 8 + /')
####        
####if __name__ == '__main__':
####    try:
####        unittest.main()
####    except SystemExit as inst:
####        if inst.args[0] is True: # raised by sys.exit(True) when tests failed
####            raise
####
