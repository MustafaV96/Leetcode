class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:        
        count = 0
        tempMag = magazine
        
        for i in ransomNote:
            if i in tempMag:
                tempMag = tempMag.replace(i,'',1)
                count = count + 1
        
        if count == len(ransomNote):
            return True
        else:
            return False