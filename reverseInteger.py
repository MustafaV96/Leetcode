#Given a signed 32-bit integer x, return x with its digits reversed. 
#If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
#Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

class Solution:
    def reverse(self, x: int) -> int:
        mylist = []
        negative = ''

        for x in str(x):
            if x == '-':
                negative = x
            else:
                mylist.append(x)

        reverseNum = negative

        for i in mylist[::-1]:
            reverseNum = reverseNum + str(i)

        if int(reverseNum) >= pow(2, 31)-1 or int(reverseNum) <= pow(-2, 31):
            return 0

        return int(reverseNum)