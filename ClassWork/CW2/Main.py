__author__ = "Haim Adrian"

from Functions import *


def ex1():
    print("ex1: (myList2Text)")
    lst = [1, ' cow, ', 2, ' geese ', 3, ' chickens ', 5.5, ' Sandwiches ', 3, 2.0, ' Liters ', 'of ', 'hell', '.']
    print("List: " + str(lst))
    print("Result: " + str(myList2Text(lst)))
    print()


def ex2():
    print("ex2: (myListMean)")
    lst = [1.0, 'abc', 12, 'aaa', '1000', 'hello', 'aaaaa', 2, '1223']
    myListMean(lst)
    print()


def ex3():
    print("ex3: (list_files)")
    currDirFiles = list_files()
    tempDirFiles = list_files('C:/temp')
    print("Files under current dir: ")
    print("\n".join(currDirFiles))
    print("Files under temp dir: ")
    print("\n".join(tempDirFiles))
    print()


def ex4():
    print("ex4: (create_3darray)")
    print(create_3darray((2, 3, 4)))
    print()


def ex5():
    print("ex5: (myRot13)")
    dummy = '!Nn\nz\ttT \\n?'
    text = 'Pnrfne pvcure?\n V zhpu cersre\t Pnrfne fnynq!'
    print("myRot13({})".format(repr(dummy)) + " = " + repr(myRot13(dummy)))
    print("myRot13({})".format(repr(text)) + " = " + repr(myRot13(text)))
    print()


def ex6():
    print("ex6: (countMyWords)")
    text = 'Hello Hello We Do Hi no No no we Donot Hey HE he heY'
    wordCounts = countMyWords(text)
    print("Text: " + text)
    print("{:<20} {}".format('Word', 'Occurrences'))
    for myKey, myLabel in wordCounts.items():
        print("{:<20} {}".format(myKey, myLabel))
    print()


def ex7():
    print("ex7: (robot_dist)")
    [up, down, left, right] = [15, 12, 7, 3]
    print("Moves: up={}, down={}, left={}, right={}".format(up, down, left, right))
    origin = (0, 0)
    distAndAngle = robot_dist(up, down, left, right, origin)
    print("Distance: {}\nAngle: {}".format(distAndAngle[0], distAndAngle[1]))
    print()


ex1()
ex2()
ex3()
ex4()
ex5()
ex6()
ex7()

