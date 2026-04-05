from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        INF = 2147483647
        queue = deque()
        visited = set()
        
        # First pass: add all treasure chests to the queue with distance 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:  # Treasure chest
                    queue.append((r, c, 0))  # (row, col, distance)
                    visited.add((r, c))
        
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up
        
        # BFS starting from all treasure chests simultaneously
        while queue:
            r, c, distance = queue.popleft()
            
            # Update the grid with the current distance
            grid[r][c] = distance
            
            # Check all four adjacent cells
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                # Check if new position is valid, not water, and not visited
                if (0 <= nr < ROWS and 0 <= nc < COLS and 
                    grid[nr][nc] != -1 and (nr, nc) not in visited):
                    
                    # Mark as visited to avoid processing again
                    visited.add((nr, nc))
                    
                    # Add to queue with incremented distance
                    queue.append((nr, nc, distance + 1))