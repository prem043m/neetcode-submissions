class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()

        for row in range(9):
            for col in range(9):
                val = board[row][col]

                if val == '.':
                    continue
                row_key = f"row_{row}_{val}"
                col_key = f"col_{col}_{val}"
                box_key = f"box_{row//3}_{col//3}_{val}"

                if row_key in seen or col_key in seen or box_key in seen:
                    return False
                seen.add(row_key)
                seen.add(col_key)
                seen.add(box_key)
        return True
