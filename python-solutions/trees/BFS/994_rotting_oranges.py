from typing import List


# problem of graph traversal and zigzag order traversal where you keep track of levels
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        rows = len(grid)
        cols = len(grid[0])

        queue = []

        mins = 0  # levels

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    queue.append((i, j, mins))

        # in number of islands problem ,  while loop is inside the nested for loop
        # here we needed to traverse the graph first to see where are all the 2s
        while queue:
            r, c, mins = queue.pop(0)
            if r > 0 and grid[r-1][c] == 1:
                grid[r-1][c] = 2
                queue.append((r-1, c, mins+1))  # adding a tuple to the queue

            if r < rows-1 and grid[r+1][c] == 1 :
                grid[r-1][c] = 2
                queue.append((r-1, c, mins+1))

            if c > 0 and grid[r][c-1] == 1:
                grid[r][c-1] = 2
                queue.append((r-1, c, mins+1))

            if c < cols-1 and grid[r][c+1] == 1:
                grid[r][c+1] = 2
                queue.append((r, c+1, mins+1))

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    return -1

        return mins

