# https://leetcode.com/problems/valid-anagram/description/
"""method 1"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        s_dict ={}
        t_dict={}
        if len(s)!=len(t):
            return False
        for i in s:
            if i in s_dict:
                s_dict[i]=s_dict[i]+1
            else:
                s_dict[i]=1
        for i in t:
            if i in t_dict:
                t_dict[i]=t_dict[i]+1
            else:
                t_dict[i]=1
        
        for i in s_dict:
            if i in t_dict:
                if s_dict[i]!=t_dict[i]:
                    return False
            else:
                return False
        return True

"""method 2"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
   
        if "".join(sorted(s))=="".join(sorted(t)):
            return True
        else:
            return False
