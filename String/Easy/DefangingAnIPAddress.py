# https://leetcode.com/problems/defanging-an-ip-address/

class Solution:
    def defangIPaddr(self, address: str) -> str:
        i = 0
        while i < len(address):
            if address[i] == '.':
                address = address[:i] + "[.]" + address[i+1:]
                i = i + 3
            else:
                i = i + 1
        return address


print(Solution().defangIPaddr("1.1.1.1"))
print(Solution().defangIPaddr("255.100.50.0"))
