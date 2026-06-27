class Solution:
    def addDigits(self, num: int) -> int:
        
        while(num>=10):
            x=0
            while(num>0):

                d=num%10
                x+=d
                num//=10
            num=x
        return num
        