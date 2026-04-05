from collections import deque
class Solution:

    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        if not grid or not grid[0]:
            return
            
        ROWS, COLS = len(grid), len(grid[0])
        INF = 2147483647
        queue = deque()
        
        # First pass: add all treasure chests to the queue
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:  # Treasure chest
                    queue.append((r, c))
                    
        # BFS starting from all treasure chests simultaneously
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up
        
        while queue:
            r, c = queue.popleft()
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                # Check if the new position is valid and is land (not water or already visited)
                if (0 <= nr < ROWS and 0 <= nc < COLS and 
                    grid[nr][nc] != -1 and grid[nr][nc] > grid[r][c] + 1):
                    # Update the distance and add to queue
                    grid[nr][nc] = grid[r][c] + 1
                    queue.append((nr, nc))
        
        