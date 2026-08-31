from collections import Counter

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        objects_to_check = board
        for i in range(9):
            column = [board[j][i] for j in range(9)]
            objects_to_check.append(column)

        submatrix = []
        shiftx = 0
        shifty = 0
        x = 0
        y = 0
        i = 0
        while i < 81:
            if x == 3:
                x = 0
                y += 1
            # print(x + shiftx, y + shifty)
            submatrix.append(board[y + shifty][x + shiftx])
            if x <= 2:
                x += 1
            if y == 3:
                y = 0
            i += 1
            if i % 9 == 0:
                # print("reset")
                y = 0
                x = 0
                if shiftx < 6:
                    shiftx += 3
                elif shiftx == 6:
                    shiftx = 0
                    shifty += 3

                objects_to_check.append(submatrix)
                submatrix = []

        for object in objects_to_check:
            counter = Counter(object)
            counter["."] = 0
            # print(counter.values())
            for value in counter.values():
                if value >= 2:
                    return False

        return True
        

