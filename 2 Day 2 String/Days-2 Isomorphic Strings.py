'''
Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

 

Example 1:

Input: s = "egg", t = "add"
Output: true
Example 2:

Input: s = "foo", t = "bar"
Output: false
Example 3:

Input: s = "paper", t = "title"
Output: true
 

Constraints:

1 <= s.length <= 5 * 104
t.length == s.length
s and t consist of any valid ascii character.
'''

#one Method this method pass 34 text but not all

class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) == len(t) and len(set(s)) == len(set(t)):
            return True
        else:
            return False

# Second Method  this passed all tests
class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):    
        return False

	s_to_t = {}             
	t_to_s = {}             

	for i in range(len(s)):
	print(i,"=")
	if s[i] in s_to_t and s_to_t[s[i]] != t[i]:
	    print("yes", s[i], s_to_t,s_to_t[s[i]], t[i])
	    return False    
	if t[i] in t_to_s and t_to_s[t[i]] != s[i]:
	    print("2 yes", t[i],t_to_s,  t_to_s[t[i]],s[i] )
	    return False   

	s_to_t[s[i]] = t[i] 
	t_to_s[t[i]] = s[i] 

	return True 
