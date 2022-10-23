from typing import List, Dict, Tuple
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        return self.KMP2((s+s)[1:-1], s) != -1

    def KMP(self,s: str, t:str) -> int:
        next = self.getNext(t)
        #next[i]代表 0到i-1 前后缀相同的最大长度， 也代表在i处不匹配时应跳转到的下一个idx位置（从0开始算）
        # 如 t=ABABC ， next应该为00012, ABAAC对应00011，AABABC对应001010这叫手算next数组，也要会。
        si, ti = 0, 0
        while si < len(s):
            if s[si] == t[ti]:
                si+=1
                ti+=1
                if ti == len(t):
                    return si-ti
            else:
                if ti == 0:
                    si += 1
                else:
                    ti = next[ti]
        else:
            return -1

    def getNext(self, t: str) -> List[int]:
        if len(t) == 0:
            return []
        elif len(t) == 1:
            return [0]
        next =[0,0]
        pre_len = 0
        idx = 2  # 从2开始算，其实也可以从1开始算，然后while idx <len(t)-1
        while idx < len(t):
            if t[idx-1] == t[pre_len]:
                next.append(pre_len+1)
                pre_len+=1
                idx+=1
            else:
                if pre_len == 0:
                    next.append(0)
                    idx+=1
                else:
                    pre_len = next[pre_len]
        return next

    def getNext2(self, t: str) -> List[int]:
        length = len(t)
        if length <= 1:
            return [0]*length
        idx, pre_len, next = 1, 0, [0,0]
        while idx + 1 < len(t):
            if t[idx] == t[pre_len]: # idx是从1开始还是从2开始仅在此处有区别，其他都一样
                next.append(pre_len+1)
                pre_len+=1
                idx+=1
            else:
                if pre_len == 0:
                    next.append(0)
                    idx+=1
                else:
                    pre_len = next[pre_len]
        return next
    def getNext3(self,t:str)->List[int]:
        len_t = len(t)
        if len_t<=1:
            return [0]*len_t
        next = [0,0]
        pre_len = 0
        idx = 2
        while idx < len_t:
            if t[idx-1] == t[pre_len]:  #别忘了idx-1
                idx +=1
                pre_len+=1
                next.append(pre_len)
            else:
                if pre_len == 0:
                    idx += 1
                    next.append(0)
                else:
                    pre_len = next[pre_len]
        return next




if __name__ == "__main__":
    # test()
    sol = Solution()
    # print(sol.getNext("ABABC"))
    # print(sol.getNext("ABAAC"))
    # print(sol.repeatedSubstringPattern("abcabcabcabc"))
    # assert(sol.repeatedSubstringPattern("abab"))
    # assert(sol.repeatedSubstringPattern("aba"))
    s = "ABCB"
    t = "ABB"
    print(sol.KMP(s,t))
