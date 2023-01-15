# diziden gelen değerler blok uzunlukları olarak düşünülürse, yağmur yağdığında blokların arasında kalan kaç blokluk alana yağmur suyu dolacağı hesaplanır. 
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        # bu şekilde de kod doğru çalışıyor ancak leetcode bu kullanımı kabul etmiyor. Temiz kod açısından bu kullanım daha iyi .
        # curr_max = 0
        # max_left = [curr_max:= max(curr_max, h) for h in height]
        # print(max_left)
        # curr_max = 0
        # max_right = [curr_max:= max(curr_max, h) for h in reversed(height)]
        # print(max_right)
        # max_right.reverse()
        # return sum([min(max_left[i], max_right[i]) - height[i] for i in range(len(height))])

        curr_max = 0
        max_left = []
        for h in height:
            curr_max = max(curr_max, h)
            max_left.append(curr_max)
        
        curr_max = 0
        max_right = []
        for h in reversed(height):
            curr_max = max(curr_max, h)
            max_right.append(curr_max)

        max_right.reverse()
        return sum([min(max_left[i], max_right[i]) - height[i] for i in range(len(height))])

        


solution = Solution()
#height = [4,2,0,3,2,5] # output = 9
height =[0,1,0,2,1,0,1,3,2,1,2,1]  # output = 6
result = solution.trap(height)
print(result) 