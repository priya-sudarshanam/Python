import math, sys, isTriangle
from isTriangle import *

def lcm(a,b):
    listA = []
    maxX = -sys.maxint - 1
    grtNum = a if a > b else b
    smlNum = b if grtNum == a else a
    for i in range(1, int((grtNum/2)+1)):
        if (((a % i) == 0) and ((b % i) == 0)):
           if i > maxX:
              maxX = i
   
    gcf = (smlNum / maxX) * grtNum

    return "GCF of %s and %s:  %s" %(a,b,gcf)
    
#print lcm(330,65)
def digitSum(d):
    sumD = 0
    for i in str(d):
       sumD += int(i)
    if len(str(sumD)) > 1:
        return digitSum(sumD)
    else:
        return sumD

#print digitSum(149)

def sumNum35(d):
   sumN = 0
   for i in range(1,d):
       if ((digitSum(i) in [3,6,9]) or (str(i)[-1] in ['0','5'])):
     #      print i
           sumN += i
   return sumN

def isPalindrome(s):
    i = 0
    j = len(str(s))-1
    k = math.ceil(len(str(s))/2)
    while i < k + 1 and j > k - 1:
        if str(s)[i] != str(s)[j]:
          return False
          break
        i += 1
        j -= 1
    return True

def largestPalindrome():
    bigPalindrome = -sys.maxint - 1
    for i,j in zip(range(999,100,-1),range(999,100,-1)):
        if isPalindrome(i*j):
            if i*j > bigPalindrome:
                bigPalindrome = i*j
                
    return bigPalindrome
         
#largestPalindrome()

def splPyth(tot):
    for a in range(1, int((tot+1)/3)):
        for b in range(a+1, int((tot+1)/2)):
            c = tot - a - b
            if (a*a + b*b == c*c):
                print a,b,c
    
#splPyth(1000)

def largProd(s):
    ctr = 0
    maxX = 0    
    for i in range(len(s)-13):
        pdt = 1
        for x in range(i,i+13):
          pdt *= int(s[x])
        if pdt > maxX:
          maxX = pdt
        
    print maxX

largProd('73167176531330624919225119674426574742355349194934\
96983520312774506326239578318016984801869478851843\
85861560789112949495459501737958331952853208805511\
12540698747158523863050715693290963295227443043557\
66896648950445244523161731856403098711121722383113\
62229893423380308135336276614282806444486645238749\
30358907296290491560440772390713810515859307960866\
70172427121883998797908792274921901699720888093776\
65727333001053367881220235421809751254540594752243\
52584907711670556013604839586446706324415722155397\
53697817977846174064955149290862569321978468622482\
83972241375657056057490261407972968652414535100474\
82166370484403199890008895243450658541227588666881\
16427171479924442928230863465674813919123162824586\
17866458359124566529476545682848912883142607690042\
24219022671055626321111109370544217506941658960408\
07198403850962455444362981230987879927244284909188\
84580156166097919133875499200524063689912560717606\
05886116467109405077541002256983155200055935729725\
71636269561882670428252483600823257530420752963450')
                
            
