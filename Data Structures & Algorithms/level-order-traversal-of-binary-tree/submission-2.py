from collections import deque

class Solution:
    def levelOrder(self, root):
        queue = deque([root])

        output = []

        while queue:
            level_output = []
            for i in range(len(queue)):
                node = queue.popleft()
                if node:
                    level_output.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)


            if level_output:
                output.append(level_output)
        

        return output
                
            
