
# Create list (sums)
class Solution:
    sums = [-9999999]
    count = 0
    
    def maxSubArray(self, myList):
        copy = myList.copy()
        listLength = len(myList)

        if (len(myList) == 1) & (Solution.count == 0):
            return(myList[0])

        for i in range(listLength):
            listSum = sum(myList)
            if listSum > Solution().sums[0]:
                Solution.sums.clear()
                Solution.sums.append(sum(myList))

            myList.pop()

            if  i == listLength - 1:
                Solution.count += 1
                copy.pop(0)
                myList = copy
                Solution().maxSubArray(myList)

        if Solution.count == listLength:
            return Solution.sums[0]
        
print(Solution().maxSubArray([1]))


# sums = [-99999999999999999]
# count = 0

# def shrink(myList):
#     global count
#     copy = myList.copy()
#     listLength = len(myList)

#     for i in range(listLength):
#         listSum = sum(myList)
#         if listSum > sums[0]:
#             sums.clear()
#             sums.append(sum(myList))
#             sums.append(myList.copy())

#         myList.pop()

#         if  i == listLength - 1:
#             count += 1
#             copy.pop(0)
#             myList = copy
#             shrink(myList)

#     if count == listLength:
#         return sums[0]
    

# print(shrink([-2,1,-3,4,-1,2,1,-5,4]))