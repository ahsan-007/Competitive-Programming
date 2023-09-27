# https://leetcode.com/problems/decoded-string-at-index/description/?envType=daily-question&envId=2023-09-27

class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        decoded_str_length = 0
        for ch in s:
            if ch.isdigit():
                decoded_str_length = decoded_str_length * int(ch)
            else:
                decoded_str_length = decoded_str_length + 1

        i = len(s) - 1
        while i >= 0:
            if s[i].isdigit():
                decoded_str_length = decoded_str_length // int(s[i])
                k = k % decoded_str_length
            else:
                if k == decoded_str_length or k == 0:
                    return s[i]
                decoded_str_length = decoded_str_length - 1
            i = i - 1


print(Solution().decodeAtIndex(s="leet2code3", k=10))
print(Solution().decodeAtIndex(s="ha22", k=5))
print(Solution().decodeAtIndex(s="a2345678999999999999999", k=1))
print(Solution().decodeAtIndex(s="b23", k=6))
print(Solution().decodeAtIndex(s="c3", k=4))
print(Solution().decodeAtIndex(s="a2b3c4d5e6f7g8h9", k=9))
print(Solution().decodeAtIndex(
    s="gc8hoa2l4lyc7cx6grev7o2qgmolppnwwgexaur2v8paml69syh2tavusb4jthoqelszpmkq2l3jem2aezlhy5c8uaibvyowbjb2", k=874960845))
