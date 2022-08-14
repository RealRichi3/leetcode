class Solution:
    def maxArea(self, height):
        max_area = 0
        l, r = 0, -1
        
        for i in height:
            lh, rh = height[l], height[r]
            max_area = max(max_area, min(rh, lh) * abs(len(height) + r - l))
            if lh < rh:
                l += 1
            if rh < lh:
                r -= 1
            if rh == lh:
                l += 1

        return max_area

height = [1,8,6,2,5,4,8,3,7]
print(Solution().maxArea(height))