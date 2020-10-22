import functions as fun

List1 = [1, 2, 3.3, 7.7, 5.0]
List2 = [1, 3, 7, 5, 3, 2]
List3 = ['C', 'a', 'c', 'X', 'v', 'b', 'C', 'b', 'a', 'A']

# 1
print ('Max of three:', fun.MaxOfThree(List1[0], List1[3], List1[2]))
print ('\n')

# 2
print ('Sum:', fun.mySum(List1))
print ('Multiply:', fun.myMultiply(List1))
print ('\n')

# 3
MeanVal = fun.myMean()
print ('Mean:', MeanVal)
print ('\n')

# 4
fun.myStars(List2)
print ('\n')

# 5
secondTop, secondBottom = fun.mySecondBest(List1)
print ('Second Top:',secondTop)
print ('Second Bottom', secondBottom)
print ('\n')

# 6
print (fun.mySort(List3))
print ('\n')

# 7
print (List3)
print (fun.myChar2Num(List3))
print ('\n')
