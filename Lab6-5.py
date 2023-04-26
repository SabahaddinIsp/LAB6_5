# QUESTION-1

def function(a,b):
    y = []
    for x in a:
        for z in b:
            if x == z:
                y.append(x)
    return y

# QUESTION-2
def function2(a):
    z = []
    for x in a:
        y = x[::-1]
        if y == x:
            z.append(x)
    return z

list1 = [1,2,3,4]
list2 = [2,3]
print(function(list1,list2))

list3 = ["abba","abc","aa"]
print(function2(list3))


# QUESTION-3
def primes(list1):
    list2 = []
    for num in list1:
        prime = [True for i in range(num + 1)]
        a = 2
        while (a * a <= num):
            if (prime[a] == True):
                for i in range(a * a, num + 1, a):
                    prime[i] = False
            a += 1
        for a in range(2, num + 1):
            if prime[a]:
                if num == a:
                    list2.append(num)
    return list2
list4= [2,3,5,8,9,14,47]
print(primes(list4))


# QUESTION-4

def function4(word,wordList):
    charList = []
    newList = []
    for x in word:
        charList.append(x)
    for y in wordList:
        tmpList = []
        for c in y:
            tmpList.append(c)
        a = set(charList)
        b = set(tmpList)
        if a == b:
            newList.append(y)

    return newList

wordList1 =  ["enlists", "google", "inlets", "banana"]
word1 = "listen"

print(function4(word1,wordList1))


