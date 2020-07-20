from Functions import *


def ex1():
    print("ex1: (MaxOfThree)")
    [a, b, c] = [4, 2, 6]
    print('ex1: a={}, b={}, c={}'.format(a, b, c))
    print("Maximum is: ", maxOfThree(a, b, c))
    print()


def ex2():
    print("ex2: (MySum, MyMul)")
    arr = [1, 2, 3, 4, 5]
    print("arr: ", arr)
    print("Sum is: ", mySum(arr))
    print("Mul is: ", myMul(arr))
    print()


def ex3():
    print("ex3: (MyMean)")
    mean = myMean()
    print("Mean: ", mean)
    print()


def ex4():
    print("ex4: (MyStars)")
    arr = [3, 9, 7]
    myStars(arr)
    print()


def ex5():
    print("ex5: (SecondBest)")
    arr = [1, 2, 3, 4]
    result = secondBest(arr)
    print("SecondMax=" + str(result[0]) + ", SecondMin=" + str(result[1]))
    print()


def ex6():
    print("ex6: (MySort (Quick Sort))")
    arr = [6, 2, 3, 1, 7, 4]
    arr2 = ['a', 'c', 'v', 'b', 'b', 'a']
    print("Arrays before sort: ")
    print(arr, " (" + str(len(arr)) + ")")
    print(arr2, " (" + str(len(arr2)) + ")")
    mySort(arr, 0, len(arr) - 1)
    mySort(arr2, 0, len(arr2) - 1)
    print("Arrays after sort: ")
    print(arr)
    print(arr2)
    print()


def ex7():
    print("ex7: (MyChar2Num)")
    arr = ['a', 'c', 'z', 'b', 'b', 'a']
    print("Array: ")
    print(arr, " (" + str(len(arr)) + ")")
    result = myChar2Num(arr)
    print("NumArray: ")
    print(result, " (" + str(len(result)) + ")")
    print()


def extra():
    print("Test cases for isNumeric:")
    testCases = ['0', '0.', '.2', '2.2', '123.321', '123abc', ' 0 ', '12 3', 'a', '', ' ']
    for i in testCases:
        line = "isNumeric('{}')={}".format(i, isNumeric(i))
        if isNumeric(i):
            line += ", Value={}".format(float(i))
        print(line)
    print()


ex1()
ex2()
ex3()
ex4()
ex5()
ex6()
ex7()
extra()

