"""
best tutorial https://www.khanacademy.org/computing/computer-science/algorithms/quick-sort/a/linear-time-partitioning
The elements in array[p..q-1] are "group L," consisting of elements known to be less than or equal to the pivot.
The elements in array[q..j-1] are "group G," consisting of elements known to be greater than the pivot.
The elements in array[j..r-1] are "group U," consisting of elements whose relationship to the pivot is unknown,
 because they have not yet been compared. Finally, array[r] is "group P," the pivot.

Initially, both q and j equal p. At each step, we compare A[j], the leftmost element in group U, with the pivot.
If A[j] is greater than the pivot, then we just increment j, so that the line dividing groups G and U slides over one
position to the right

If instead A[j] is less than or equal to the pivot, then we swap A[j] with A[q] (the leftmost element in group G),
increment j, and increment q, thereby sliding the line dividing groups L and G and the line dividing groups G and U
over one position to the right:

Once we get to the pivot, group U is empty. We swap the pivot with the leftmost element in group G: swap A[r] with A[q].
"""
from typing import List


class Solution:
    def partition(self, array: List[int], p, r):
        q = p
        for j in range(p, r):
            if array[j] <= array[r]:
                array[j], array[q] = array[q], array[j]
                q += 1
        array[r], array[q] = array[q], array[r]  # after partition moving pivot in between the two groups
        return q

    def quick_sort(self, array: List[int], p, r):  # p = low , r = high == pivot
        if p < r:
            pivot = self.partition(array, p, r)
            self.quick_sort(array, p, pivot-1)
            self.quick_sort(array, pivot+1, r)


n = [4, 5, 9, 8, 6, 7, 3, 2]
qs = Solution()
qs.quick_sort(n, 0, len(n)-1)
print(n)




