class Solution:
    def defangIPaddr(self, address: str) -> str:
        #1 liner return address.replace(".","[.]")
        s = ''
        for c in address:
            if c != '.':
                s += c
            else: # c == '.':
                s += '[.]'
        return s