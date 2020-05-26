from typing import List

"""
x << y
Returns x with the bits shifted to the left by y places (and new bits on the right-hand-side are zeros).
This is the same as multiplying x by 2**y.

bin()
Return the binary representation of an integer.

   >>> bin(2796202)
   '0b1010101010101010101010'

x | y
Does a "bitwise or". Each bit of the output is 0 if the corresponding bit of x AND of y is 0, otherwise it's 1.

"""


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        output = []

        for i in range(2 ** n, 2 ** (n + 1)):
            # generate bitmask, from 0..00 to 1..11
            bitmask = bin(i)[3:]
            print(bitmask)

            # append subset corresponding to that bitmask
            subs = list()
            for j in range(n):
                if bitmask[j] == '1':
                    subs.append(nums[j])

            output.append(subs)

        return output

def main():
    Solution.subsets([1,2,3])

if __name__ == '__main__':
    main()
