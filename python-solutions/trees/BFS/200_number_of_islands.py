from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        1. graph concepts/mechanisms - visited nodes , matrix traversing
        2. number of times you have to run BFS is the number of islands
        3. question says no diagonal , only horizontal and vertical
        """
        if not grid:
            return 0

        rows = len(grid)
        cols = len(grid[0])

        count = 0  # number of times you will run BFS

        for i in range(rows):
            for j in range(cols):
                queue = []  # you can use deque
                if grid[i][j] == "1":
                    queue.append((i, j))  # queue is for coordinate not the value
                    grid[i][j] = "0"
                    count += 1

                while queue:  # this is BFS , number of times BFS runs is number of islands
                    r, c = queue.pop(0)  # if you use deque , use popleft

                    if r > 0 and grid[r - 1][c] == "1":
                        grid[r - 1][c] = "0"
                        queue.append((r - 1, c))

                    if r < rows - 1 and grid[r + 1][c] == "1":
                        grid[r + 1][c] = "0"
                        queue.append((r + 1, c))

                    if c > 0 and grid[r][c - 1] == "1":
                        grid[r][c - 1] = "0"
                        queue.append((r, c - 1))

                    if c < cols - 1 and grid[r][c + 1] == "1":
                        grid[r][c + 1] = "0"
                        queue.append((r, c + 1))

        return count;
