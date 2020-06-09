from typing import List
from collections import Counter


class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        ans = Counter()
        # not used dictionary because we will have to use if-else statement to check , if the element doesn't exist
        # counter automatically assigns 0 valueß
        # counter creates a dictionary - key (list element), value (number of times list element has occurred)
        for domain in cpdomains:
            count, domain = domain.split()  # unwrap variable
            count = int(count)  # convert string to int
            frags = domain.split('.')
            l = len(frags)
            for i in range(l):
                ans[".".join(frags[i:])] = ans[".".join(frags[i:])] + count  # list comprehension

        return ["{} {}".format(ct, dom) for dom, ct in ans.items()] # list comprehension


def main():
    tld: List[str] = ["901 mail.com", "50 yahoo.com", "900 google.mail.com", "5 wiki.org", "5 org", "1 intel.mail.com",
                      "951 com"]
    result = Solution()
    result.subdomainVisits(tld)
    print(result)


if __name__ == '__main__':
    main()


