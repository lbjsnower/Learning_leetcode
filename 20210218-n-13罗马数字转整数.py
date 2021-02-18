class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        lm2int = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500,
                  "M": 1000}
        s_len_num = len(s)
        ans = 0
        # for i in range(s_len_num-1):
        #     if lm2int[s[i]] < lm2int[s[i+1]]:
        #         ans -= lm2int[s[i]]
        #     else:
        #         ans += lm2int[s[i]]
        # return ans+lm2int[s[-1]]
        lm2int = {'I': 1, 'IV': 3, 'V': 5, 'IX': 8, 'X': 10, 'XL': 30, 'L': 50,
                  'XC': 80, 'C': 100, 'CD': 300, 'D': 500, 'CM': 800, 'M': 1000}
        alist = ['IV', 'IX', 'XL', 'XC', 'CD', 'CM']

        s_len_num = len(s)
        i,ans = 0,0
        while i < s_len_num - 1:
            if s[i]+s[i+1] in alist:
                ans += lm2int[s[i]+s[i+1]]
                print('2--',i,s[i:i+2],lm2int.get(s[i:i+2]),ans)
                i += 2
            else:
                ans += lm2int[s[i]]
                print('1--',i,s[i],lm2int.get(s[i]),ans)
                i += 1
        return ans+lm2int[s[-1]]



s = "LVIII"
sl = Solution()
print(sl.romanToInt(s))
