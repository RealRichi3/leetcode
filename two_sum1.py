import time
start = time.time()


def twoSum(mainNums, target):
    sortedNums = mainNums.copy()
    sortedNums.sort()
    count = 0
    ans = []
    mainAns = []

    while count < len(sortedNums) - 1:
        first = sortedNums[count]
        second = sortedNums[count + 1]
        
        if first + second == target:
            ans.append(sortedNums.index(first))
            sortedNums[count] = str(first)
            ans.append(sortedNums.index(second))
            sortedNums[count] = int(first)

            mainAns.append(mainNums.index(first))
            mainNums[mainNums.index(first)] = ''
            mainAns.append(mainNums.index(second))

            return mainAns
        
        newCount = count
        copyFirst = first
        while (copyFirst + second > target) &  (newCount > 0):
            preFirst = sortedNums[newCount - 1]

            if second + preFirst == target:
                ans.append(sortedNums.index(preFirst))
                sortedNums[newCount - 1] = str(preFirst)
                ans.append(sortedNums.index(second))
                sortedNums[newCount - 1] = int(preFirst)

                mainAns.append(mainNums.index(preFirst))
                mainNums[mainNums.index(preFirst)] = ''
                mainAns.append(mainNums.index(second))

                return mainAns

            newCount -= 1
            copyFirst = first
        count += 1



print(twoSum([3,2,3], 6))
print(time.time() - start)