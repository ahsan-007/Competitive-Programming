# https://leetcode.com/problems/subdomain-visit-count/

from typing import List


class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        domain_frquency = {}
        for domain in cpdomains:
            splitted_cpdomain = domain.split(" ")
            frequency = int(splitted_cpdomain[0])
            splitted_domain = splitted_cpdomain[1].split(".")
            while len(splitted_domain) > 0:
                domain = '.'.join(splitted_domain)
                domain_frquency[domain] = domain_frquency.get(
                    domain, 0) + frequency
                splitted_domain.pop(0)

        return [f'{frequency} {domain}' for domain, frequency in domain_frquency.items()]


print(Solution().subdomainVisits(["9001 discuss.leetcode.com"]))
print(Solution().subdomainVisits(["900 google.mail.com",
                                  "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]))
