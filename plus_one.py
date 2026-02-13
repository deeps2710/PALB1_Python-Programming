class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        str1="".join(map(str, digits))
        result=int(str1)+1
        str2=str(result)
        return list(map(int, str2))
        
