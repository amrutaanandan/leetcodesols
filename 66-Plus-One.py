class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = 0
        powe = len(digits)-1
        for i in range(len(digits)):
            num += digits[i]*10**powe
            powe -= 1

        num = str(num+1)
        lis = list(num)
        
        lis = list(map(int, lis))
        return lis
