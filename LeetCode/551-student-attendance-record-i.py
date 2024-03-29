###############################################################################################
# 一次遍历
###########
# 时间复杂度：O(n)，s的长度
# 空间复杂度：O(1)
###############################################################################################
class Solution:
    def checkRecord(self, s: str) -> bool:
        A = L = 0
        for ch in s:
            if ch == 'A':
                A += 1
                L = 0
            elif ch == 'L':
                L += 1
            else:
                L = 0
            if A > 1 or L >= 3:
                return False
        return True