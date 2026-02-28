class Solution:
    def frequencySort(self, s):
        freq={}
        for char in s:
            if char in freq:
                freq[char]+=1
            else:
                freq[char]=1
        items=freq.items()
        sorted1=sorted(items, key=lambda x:(x[1],x[0]))
        result=''
        for char,frequency in sorted1:
            result+=char*frequency
        return result
