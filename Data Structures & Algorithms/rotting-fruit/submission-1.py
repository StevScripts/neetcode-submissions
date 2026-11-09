class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        time, fresh = 0,0
        
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        ROWS,COLS = len(grid), len(grid[0])

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                
                if grid[r][c] == 2:
                    q.append([r,c])

        while q and fresh > 0:
            for i in range(len(q)):
                r,c = q.popleft()
                for dr,dc in directions:
                    curRow,curCol = dr + r, dc + c
                    if curRow < 0 or curCol < 0 or curRow >= ROWS or curCol >= COLS or grid[curRow][curCol] != 1:
                        continue

                    grid[curRow][curCol] = 2
                    q.append([curRow,curCol])
                    fresh -= 1

            time += 1

        return time if fresh == 0 else -1