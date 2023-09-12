class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        s = strs[0]
        substrings = [s[i:j] for i in range(1) for j in range(i+1, len(s)+1)]
        print(substrings)
        max = 0
        flag = 0
        subs = ""
        for string in substrings:
            
            for item in strs:
                if item.startswith(string) is False:
                    flag = -1
                    break

            if len(string) > max and flag == 0:
                max = len(string)
                subs = string
            flag = 0

        return subs
