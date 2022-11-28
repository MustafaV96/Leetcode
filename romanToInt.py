class Solution:
    def romanToInt(self, s: str) -> int:
        sum = 0
        for i in range(0, len(s)):
            if (s[i] == "I"):
                if ((i+1)!=len(s)):
                    if (s[i+1] == "V" or s[i+1] == "X"):
                        sum = sum - 1
                    else: 
                        sum = sum + 1
                else:
                    sum = sum + 1
            if (s[i] == "V"):
                sum = sum + 5
            if (s[i] == "X"):
                if ((i+1)!=len(s)):
                    if (s[i+1] == "L" or s[i+1] == "C"):
                        sum = sum - 10
                    else: 
                        sum = sum + 10
                else:
                    sum = sum + 10
            if (s[i] == "L"):
                sum = sum + 50
            if (s[i] == "C"):
                if ((i+1)!=len(s)):
                    if (s[i+1] == "D" or s[i+1] == "M"):
                        sum = sum - 100
                    else: 
                        sum = sum + 100
                else: 
                    sum = sum + 100
            if (s[i] == "D"):
                sum = sum + 500
            if (s[i] == "M"):
                sum = sum + 1000
                
        return sum