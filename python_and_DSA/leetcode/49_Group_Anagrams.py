# https://leetcode.com/problems/group-anagrams/description/
"""method 1"""
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic={}
        dic_ans={}
        for word in strs:
            dic_temp={}
            for i in word:
                if i in dic_temp:
                    dic_temp[i]=dic_temp[i]+1
                else:
                     dic_temp[i]=1
            dic[word]=dic_temp
        
        for word in dic:
            if dic[word] in dic_ans:
                dic_ans[word].append(word)
            else:
                dic_ans[word]=[word]
        ans=[]
        for i in dic_ans:
            ans.append(dic_ans[i])
        return dic_ans

"""method 2"""
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic={}
        for word in strs:
            # print("word",word)
            sw="".join(sorted(word))
            # print(sw)
            if sw not in dic:
                dic[sw]=[word]
            else:
                # print(sw,dic[sw])
                dic[sw].append(word)

        return list(dic.values())

