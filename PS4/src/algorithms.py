from utilFunc import *
import copy
#Use with OR
def isEqualUsedOnlyOr(val1: str, val2: str) -> bool:
    arr1 = val1.split(" OR ")
    arr2 = val2.split(" OR ")
    arr1.sort()
    arr2.sort()
    if len(arr1) != len(arr2): return False
    for (a,b) in zip(arr1, arr2):
        if a != b:
            return False
    return True

def checkClauseInClauses(clause, clauses):
    for val in clauses:
        if isEqualUsedOnlyOr(clause,val):
            return True
    return False

#Remove duplicates with OR condition
def removeDupOr(a: list) -> list:
    arr = copy.deepcopy(a)
    i = 0
    j = 0
    while i < len(arr):
        j = i + 1
        while j < len(arr):
            if isEqualUsedOnlyOr(arr[i],arr[j]):
                del arr[j]
            else:
                j += 1
        i += 1
    return arr


def parseIntoCNF(clause: str) -> list:
    arr = clause.split(' ')
    temp = ""
    answer = []
    for val in arr:
        if val == "AND":
            answer.append(temp.strip())
            temp = ""
        elif val == "OR":
            temp += "OR "
        else:
            temp += val + " "
    answer.append(temp.strip())
    return list(dict.fromkeys(answer))



def putNegativeAlphaIntoKB(kbValues: list, alpha: str) -> list:
    copyKB, copyAlpha = copy.deepcopy(kbValues), copy.deepcopy(alpha)

    negativeAlpha = negateComplexClause(copyAlpha)
    cnfFormSet = parseIntoCNF(negativeAlpha)
    copyKB.extend(cnfFormSet)
    return list(dict.fromkeys(copyKB))


#ASCII A starts from 41
def parseClauseIntoArray(clause: str,clauseArr):
    if clause == "{}":
        return
    arr = clause.split(' OR ')
    for val in arr:
        if len(val) == 2:
            clauseArr[ord(val[1])-ord('A')] = -1
        else:
            clauseArr[ord(val[0])-ord('A')] = 1

def clauseArrIntoClause(clArr):
    res = ""
    for i in range(26):
        if clArr[i] == 1:
            res += chr(i + ord('A'))
            res += " OR "
        elif clArr[i] == -1:
            res += "-"+ chr(i + ord('A'))
            res += " OR "
    if 1 in clArr:
        return res[:-4]
    if -1 in clArr:
        return res[:-4]
    return "{}"

def evaluationCombine(clArr1: list, clArr2: list):
    if checkSimpleLiteralContradict(clArr1,clArr2) == False:
        return " "
    resArr = [0 for i in range(26)]
    count = 0
    for i in range(26):
        if count == 2:
            return " "
        if clArr1[i] * clArr2[i] == -1:
            count += 1
        resArr[i] = clArr1[i] if clArr1[i] == clArr2[i] else clArr1[i] + clArr2[i] 
    return clauseArrIntoClause(resArr)

def checkSimpleLiteralContradict(clArr1:list, clArr2:list):
    for i in range(26):
        if clArr1[i] * clArr2[i] == -1:
            return True
    return False
def plResolve(cl1: str,cl2: str)-> str:
    #Initialize array A -> Z
    clArr1 = [0 for i in range(26)]
    clArr2 = [0 for i in range(26)]
    parseClauseIntoArray(cl1,clArr1)
    parseClauseIntoArray(cl2,clArr2)
    return evaluationCombine(clArr1, clArr2)

def containsEmptyClause(new):
    return "{}" in new
def smallInLarge(small,large):
    if len(small) == 0:
        return True
    count = 0 
    for itr1 in small:
        if itr1 in large:
            count += 1
            continue    
        for itr2 in large:
            if isEqualUsedOnlyOr(itr1,itr2) == True:
                count += 1
                break
    return count == len(small)


def printArr(arr:list,resultArr:list):
    for itr in arr:
        clArr = [0 for i in range(26)]
        parseClauseIntoArray(itr,clArr)
        resultArr.append(clauseArrIntoClause(clArr))

#Write pl_resolution function
def plResolution(kbValues: list, alpha: str, resultArr: list) -> bool:
    clauses = putNegativeAlphaIntoKB(kbValues, alpha)
    new = []
    while len(clauses) > 0:
        for i in range(0,len(clauses)-1):
            for j in range(i+1,len(clauses)):
                resolvents = plResolve(clauses[i], clauses[j])
                if resolvents in clauses or resolvents == " " or checkClauseInClauses(resolvents,clauses):
                    continue
                else:
                    #print(clauses[i] + " + " + clauses[j] + " = " + resolvents)
                    new.append(resolvents)
        new = copy.deepcopy(removeDupOr(list(dict.fromkeys(new))))
        if containsEmptyClause(new):
            resultArr.append(str(len(new)))
            printArr(new,resultArr)
            return True
        if smallInLarge(new,clauses):
            resultArr.append('0')
            return False
        resultArr.append(str(len(new)))
        printArr(new,resultArr)
        clauses.extend(new)
        clauses = copy.deepcopy(removeDupOr(list(dict.fromkeys(clauses))))
        new = []
