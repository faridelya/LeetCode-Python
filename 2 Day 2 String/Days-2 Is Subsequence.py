'''
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

 

Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true
Example 2:

Input: s = "axc", t = "ahbgdc"
Output: false
 

Constraints:

0 <= s.length <= 100
0 <= t.length <= 104
s and t consist only of lowercase English letters.
 

Follow up: Suppose there are lots of incoming s, say s1, s2, ..., sk where k >= 109, and you want to check one by one to see if t has its subsequence. In this scenario, how would you change your code?
'''
# first method that pass 16 test except 17
class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        x = []
        
        if len(s) == 0:
            return True
        if s and  t: 
            for z in range(len(s)):
                bol = s[z] in t
                if bol == True:
                    continue
                else:
                    return False
            for idex , i in enumerate(s):
                x.append(t.rfind(i))

            for  ii in range( len(x)):
       
                for u in x[ii+1:]:
                    if x[ii] < u:
           
                    else:
   
                        return False
                if ii == len(x)-1:

                    return True  
                    
                    
                    
# second and best method
class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        i = 0  # index of the current character in s
        for c in t:
            if i == len(s):
                break
            if c == s[i]:
                i += 1
        return i == len(s)
        
        
        
