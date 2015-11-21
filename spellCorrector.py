import re, collections
from collections import defaultdict
import levinshtein
from levinshtein import  *

alphabet = "abcdefghijklmnopqrstuvwxyz"

def words(d):
    return re.findall('[a-z]+',d.lower())

def wordDict(d):
    wDict = defaultdict(lambda: 0)
    for i in d:
        wDict[i] += 1
    return wDict

allWords = wordDict(words(file('./big.txt').read()))

def edits1(word):
    splits = [(word[:i],word[i:]) for i in range(len(word)+1)]
    deletes = [a + b[1:] for a,b in splits if len(b) >= 1 and len(a) >=1]
    transposes = [a + b[1]+b[0]+b[2:] for a,b in splits if len(b) >1]
    replaces = [a + c + b[1:] for a,b in splits for c in alphabet if  b]
    inserts = [a+c+b for a,b in splits for c in alphabet]
    return set(inserts + transposes + replaces + deletes)

def knownEdits2(word):
    return set(e2 for e1 in edits1(word) for e2 in edits1(e1) if e2 in allWords)

def known(words):
    return set(w1 for w1 in words if w1 in allWords)

def correct(word):
    l = []
    candidates = known([word]) or known(edits1(word)) or [word]
   # return candidates
    for i in candidates:
        if levenshtein(word,i) <= 4:
            l.append(i)
    #return l
    return max(l, key = lambda w: allWords[w])    


print correct("possble")
print correct("econometric")
print correct("therea")
print correct("arrangng")
print correct("spellnig")
print correct('rsources')
print correct('lanten')
print correct('holl')
