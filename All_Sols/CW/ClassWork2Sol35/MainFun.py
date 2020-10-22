__author__ = 'Dmitry Patashov'

from FunctionList import *

# Assignment 1:
List1 = [1, ' cow, ', 2, ' geese ', 3,
         ' chickens ', 5.5, ' Sandwiches ',
         3, 2.0, ' Liters ', 'of ', 'hell', '.']

print (myList2Text(List1))
print()

# Assignment 2:
List2 = [ 1.0, 'abc', 'aaa', 2, '1000',
          'hello', 'aaaaa', 12, '1223']
List3 = [np.uint16(1), '2a', np.double(2.2), '12',
         'aaa', np.float32(11), np.float64(17), tuple('18')]

myListMean(List2)
myListMean(List3)
print()

# Assignment 3:
print (list_files())
print()

# Assignment 4:
myTuple = (2,3,5)

print (create_3darray(myTuple).shape)
print()

# Assignment 5:
myStr1 = '!Nn\nz\ttT \\n?'
myStr2 = 'Pnrfne pvcure?\n V zhpu cersre\t Pnrfne fnynq!'

print (myRot13(myStr1))
print()
print (myRot13(myStr2))
print()

# Assignment 6:
myStr3 = 'Hello Hello We Do Hi no No no we Donot Hey HE he heY'

countMyWords(myStr3)
print()

# Assignment 7:
print (robot_dist(15,12,7,3))
