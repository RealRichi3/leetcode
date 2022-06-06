import time
start = time.time()

class Solution:
    def __init__(self, mainNums=0, target=0):
        self.mainNums = mainNums
        self.target = target
        
    def checkMainList(self, args):
        '''
            Accounts for when the first and second number are the same integers
            but different index in the given list
        '''
        ans, nums, firstItem, secondItem = args

        ans.append(nums.index(firstItem))
        nums[nums.index(firstItem)] = str(firstItem)
        ans.append(nums.index(secondItem))

        return ans
    
    def twoSum(self, mainNums, target):
        sortedNums = mainNums.copy()
        sortedNums.sort()
        mainAns = []
        count = 0
        
        while count < len(sortedNums) - 1:
            first = sortedNums[count]
            second = sortedNums[count + 1]
            if first + second == target:
                mainAns = self.checkMainList([mainAns, mainNums, first, second])
                return mainAns

            newCount = count
            copyFirst = first
            while (copyFirst + second > target) &  (newCount > 0):
                preFirst = sortedNums[newCount - 1]
                if second + preFirst == target:
                    mainAns = self.checkMainList([mainAns, mainNums, preFirst, second])
                    return mainAns

                newCount -= 1
                copyFirst = first

            count += 1
            
    



print(Solution().twoSum(list(range(0, 10001)), 19999))
print(time.time() - start)