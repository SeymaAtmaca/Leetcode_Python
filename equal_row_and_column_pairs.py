import numpy as np
from typing import List
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:

        matrix = np.array(grid)
        rows = matrix.tolist()
        columns = matrix.T.tolist()

        count = 0

        for row in rows:
            for column in columns:
                if row == column:
                    count += 1

        return count