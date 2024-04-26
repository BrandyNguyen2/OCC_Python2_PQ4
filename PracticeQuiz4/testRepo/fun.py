aList = ["Bunny", "cat", "dog", "Elephant", "cow", "zebra", "GIRAFFE WITH A MONKEY"]
print(len(aList))
i = 0
largestStr = aList[i]

while i != len(aList) :
    print(aList[i])
    if len(largestStr) < len(aList[i]) :
        largestStr = aList[i]
    i += 1

print(largestStr)