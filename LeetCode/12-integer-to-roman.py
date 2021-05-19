###############################################################################################
# 从大到小依次找到能用于表示的最大数即可
###########
# 时间复杂度：O(1)，基于本题给的数字范围，时间复杂度为常数级
# 空间复杂度：O(1)
###############################################################################################
class Solution:
    def intToRoman(self, num: int) -> str:
        romanLetter = ""
        nums = [[1000, 'M'], [900, 'CM'], [500, 'D'], [400, 'CD'], [100, 'C'], [90, 'XC'], 
        [50, 'L'], [40, 'XL'], [10, 'X'], [9, 'IX'], [5, 'V'], [4, 'IV'], [1, 'I']]
        
        for thisNum, Letter in nums:
            while(num>=thisNum):
                num -= thisNum
                romanLetter += Letter

        return romanLetter