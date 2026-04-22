import os


os.system("cls")

s = "   fly me   to   the moon  "

s = s.split(" ")
words = []

for x in s:
    if x != "":
        words.append(x)

print(len(words[-1]))


print(words)

print("---------------------------------------------")
s = ["h", "e", "l", "l", "o"]

print(s)
for x in range(len(s) // 2):
    s[x], s[(len(s) - 1) - x] = s[(len(s) - 1) - x], s[x]

print(s)

print("---------------------------------------------")
s = "loveleetcode"


def firstUniqChar(s: str):
    for index, x in enumerate(s):
        contador = 0
        for i in s:
            if x == i:
                contador += 1
                if contador > 1:
                    contador = 0
                    break

        if contador == 1:
            return index

    return -1


print(firstUniqChar(s))
print("---------------------------------------------")

x = 121


def isPalindrome(x: str):
    string = str(x)
    lenght = len(string)
    lista = []
    resultado = ""
    for a in string:
        lista.append(a)

    for b in range(lenght // 2):
        lista[b], lista[(lenght - 1) - b] = lista[(lenght - 1) - b], lista[b]

    for c in lista:
        resultado += c

    if resultado == str(x):
        return True

    return False


print(isPalindrome(x))
print("---------------------------------------------")


haystack = "otomatetomas"
needle = "tomas"


def strStr(haystack, needle):
    """
    :type haystack: str
    :type needle: str
    :rtype: int
    """
    h = len(haystack)
    n = len(needle)

    word = ""
    index = 0
    for a in range(h):
        word = haystack[a : a + n]
        index += 1
        if word == needle:
            return index - 1

    return -1


print(strStr(haystack=haystack, needle=needle))

print("---------------------------------------------")

nums = [2, 7, 11, 15]
target = 9


def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    index1 = 0
    lenght = len(nums)
    for x in range(lenght):
        index1 += 1
        index2 = 0

        for j in range(1, lenght):
            index2 += 1

            if nums[x] + nums[j] == target:
                return [index1 - 1, index2]


print(twoSum(nums=nums, target=target))

print("---------------------------------------------")

n = 2


def fizzBuzz(n):
    """
    :type n: int
    :rtype: List[str]
    """
    result: list[str] = []

    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            result.append(str("FizzBuzz"))
        elif i % 3 == 0:
            result.append(str("Fizz"))
        elif i % 5 == 0:
            result.append(str("Buzz"))
        else:
            result.append(str(i))
    return result


print(fizzBuzz(n=n))

print("---------------------------------------------")

s = "Hello"


def toLowerCase(s: str):
    """
    :type s: str
    :rtype: str
    """
    lower: str = ""
    ABECEDARIO = {chr(i): chr(i + 32) for i in range(65, 91)}

    for i in s:
        if i in ABECEDARIO:
            lower += ABECEDARIO.get(i)
        else:
            lower += i
    return lower


print(toLowerCase(s))

print("---------------------------------------------")
n = 16


def isPerfectSquare(num):
    """
    :type num: int
    :rtype: bool
    """
    sqr = num**0.5
    if sqr % 1 == 0:
        return True
    return False


print(isPerfectSquare(n))


print("---------------------------------------------")

flowerbed = [1, 0, 0, 0, 1]
n = 2


def canPlaceFlowers(flowerbed, n):
    """
    :type flowerbed: List[int]
    :type n: int
    :rtype: bool
    """
    length = len(flowerbed)

    for i in range(length):
        if flowerbed[i] == 0:
            anterior = 0 if i == 0 else flowerbed[i - 1]
            siguiente = 0 if i == length - 1 else flowerbed[i + 1]

            if anterior == 0 and siguiente == 0:
                flowerbed[i] = 1
                n -= 1

                if n == 0:
                    return True
    return False


print(canPlaceFlowers(flowerbed, n))
