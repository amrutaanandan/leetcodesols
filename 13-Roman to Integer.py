class Solution:
    def romanToInt(self, s: str) -> int:
        numeralsDict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        s = s.strip('\"')
        num = 0
        for i in range(len(s)):
            if (i < len(s)-1) and (numeralsDict[s[i]] < numeralsDict[s[i+1]]):
                num -= numeralsDict[s[i]]
            else:
                num += numeralsDict[s[i]]
        return num
