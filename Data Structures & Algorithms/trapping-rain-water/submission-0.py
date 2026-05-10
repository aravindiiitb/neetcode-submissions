class Solution:
    def trap(self, height: List[int]) -> int:
        i = 0
        while height[i] == 0:
            i += 1
        
        j = i + 1

        totalWater = 0
        curr_area_to_subtract = 0
        
        while j != len(height):
            heightOfLeftWall = height[i]          

            while height[j] == 0:
                j += 1

            heightOfRightWall = height[j]

            if heightOfRightWall >= heightOfLeftWall:
                curr_area = heightOfLeftWall * (j - i - 1)
                for k in range(i, j):
                    curr_area_to_subtract += height[k]
                curr_area -= curr_area_to_subtract

                totalWater += curr_area
                i = j
            j += 1
        
        return totalWater

            
