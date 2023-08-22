# в одномерном массиве состоящем из н вечественных чисел, вычислить:
# a) номер максимального элемента
# b) сумму элементов между первым и вторым отрицательными элементами массива
# c) отсортировать массив по возрастанию элементов по модульу
import random
someList = []
lenSomeList = int(input('Введите длину массива '))
for i in range(lenSomeList):
    someList.append(random.randint(-100, 100))
print(someList)
print('a) ', someList.index(max(someList)))
indexNumber1 = 0
indexNumber2 = 0
indexNegativeNumber1 = 0
indexNegativeNumber2 = 0
for i in range(len(someList)):
    if someList[i] < 0:
        indexNegativeNumber1 = i
        break
for i in range(len(someList)):
    if someList[i] < 0 and someList[i] != someList[indexNegativeNumber1]:
        indexNegativeNumber2 = i
        break
sumIndexs = sum(someList[indexNegativeNumber1+1:indexNegativeNumber2])
print('b) ', sumIndexs)
print('c) ', sorted(someList, key=abs))
print(indexNegativeNumber1, indexNegativeNumber2)
