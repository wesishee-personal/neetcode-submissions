class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check horizontal rows
        horizontalRowsValid = self.iterateRows(board)
        if horizontalRowsValid != True:
            return False
        # collect vertical rows
        verticalRows = self.getVerticalRows(board)
        verticalRowsValid = self.iterateRows(verticalRows)
        if verticalRowsValid != True:
            return False
        squaresAreValid = self.iterateSquares(board)
        if not squaresAreValid:
            return False
        return True

    def iterateRows(self, board: List[List[str]]):
        for row in board:
            isValid = self.isValidRow(row)
            if isValid != True:
                return False
        return True

    def iterateSquares(self, board):
        squares = self.getSquareValues(board)
        for row in squares:
            square_is_valid = self.isValidRow(row)
            if not square_is_valid:
                return False
        return True

    def getVerticalRows(self, board):
        verticalRows = []
        i, j = 0, 0
        while i < len(board):
            currentColumn = []
            while j < len(board):
                currentColumn.append(board[j][i])
                j += 1
            verticalRows.append(currentColumn)
            i += 1
            j = 0
        return verticalRows

    def isValidRow(self, row: List[str]) -> bool:
        seen = set()
        for value in row:
            if value in seen:
                return False
            elif value != ".":
                seen.add(value)
        return True

    def getSquareValues(self, board):
        square_row = 0
        square_column = 0
        squares = []
        while square_row < len(board):
            while square_column < len(board[0]):

                square = board[square_row][square_column:square_column + 3]
                square += board[square_row + 1][square_column:square_column + 3]
                square += board[square_row + 2][square_column:square_column + 3]

                squares.append(square)
                square_column += 3

            square_column = 0
            square_row += 3

        return squares

    def isValidSquare(self, square: List[str]) -> bool:
        squareMap = [0] * 9
        iterator = 0
        for i in range(9):
            if not 48 <= ord(squareMap[square[i]]) <= 57:
                continue
            squareMap[square[i]] += 1
            if squareMap[square[i]] > 1:
                return False
            i += 1