# https://leetcode.com/problems/maximum-number-of-non-overlapping-palindrome-substrings/description/?envType=daily-question&envId=2026-09-15

class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        def maxPalindromesUtil(s, i, j):
            if i < 0 or j >= len(s) or s[i] != s[j]:
                return -1, -1

            if j-i+1 >= k:
                return i, j

            return maxPalindromesUtil(s, i-1, j+1)

        if k == 1:
            return len(s)

        i = 0
        while i < len(s):
            start, end = maxPalindromesUtil(s, i-1, i)
            if start != -1:
                return self.maxPalindromes(s[end+1:], k) + 1

            start, end = maxPalindromesUtil(s, i, i)
            if start != -1:
                return self.maxPalindromes(s[end+1:], k) + 1

            i = i + 1

        return 0


print(Solution().maxPalindromes(s="abaccdbbd", k=3))
print(Solution().maxPalindromes(s="adbcda", k=2))
print(Solution().maxPalindromes(s="fttfjofpnpfydwdwdnns", k=2))
print(Solution().maxPalindromes(
    s="zqzogfurlfmrnlffuipuupidkfhkggkhdrzezghwziopoinnsdkwkymhygonbiizmmmmzjhmyczzlz", k=2))
print(Solution().maxPalindromes(
    s="pwfptewrvpeepvrwetpfuegohrdleteldrhogeuyricjoepiwncucnwipeojebpajdpwsdpnnpdswpdjapwqxifmkcmmoztsxiixstzommckcyqkdmxcjfjcxmdkqychcrfclblcdmmdclblcfrcxxpmyxciicxympxxvtwrrenfssfnerrwtvkdaddevwedewveddadkrsirisltnikcckintlsirixgbjvoetsasteovjbgxwtgkdlsuusldkgtwmnzofrxmhsshmxrfozswtlmylpqvvqplymltwrvxhkmgrwwrgmkhxvrwhtqvabzwyllywzbavqtzkibseqhgsmzifizmsghqezdifukpksbbskpkufigsakogkerjjrekgokasquzdujtoonwnootjudzupqpafqofiusjsuifoqfafbtvflzfauuafzlfvtbfkpheguosijlzljisougehsqtglzqrzfhmseptatpesmhfzrppdvlfmnvvnmflvdppggnxtyrdsgsdrytxnggcmyqcbdfparbggbrapfdbcqxenpjehvvhejpnexnirypjvmwpwmvjpyrintqsxxc", k=2))
