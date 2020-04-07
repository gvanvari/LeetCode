class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        L = len(s)
        if L < k: return s[::-1]
        if L > k and L <= k * 2:
            return s[:k][::-1] + s[k:]
        ans = ''
        for i in range(0, L, 2 * k):
            ans += (s[i:i + k][::-1] + s[i + k:i + 2 * k])
        return ans
