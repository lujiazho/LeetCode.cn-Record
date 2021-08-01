###############################################################################################
# 难点在于分析是否会陷入无限增长而不循环的境地，证明可知不会
###########
# 时间复杂度：O(logn), 得到数字平方和只需要logn，而循环次数也是低于logn的
# 空间复杂度：O(logn)，哈希消耗，最多也就保存进入循环前的所有数，具体分析较复杂
###############################################################################################
class Solution:
    def isHappy(self, n: int) -> bool:
        # 分析可知不可能不进入循环而无限放大
        def big(x):
            return int(x)**2
        set_ = set()
        while n != 1:
            if n not in set_:
                set_.add(n)
            else:
                return False # 情况2，进入循环
            n = sum(map(big, list(str(n))))
        return True # 情况1，得到1