class Spreadsheet:
    sheet: list[dict[int, int]]  # sheet[AAA][12345] = value
    rows: int
    @staticmethod
    def cell_to_row(cell: str) -> tuple[int, int]:
        col = ord(cell[0]) - ord('A')
        row = int(cell[1:])
        return row, col

    def __init__(self, rows: int):
        self.rows=rows
        self.sheet = [defaultdict(lambda: 0) for _ in range(rows+1)]

    def setCell(self, cell: str, value: int) -> None:
        row, col = self.cell_to_row(cell)
        self.sheet[row][col] = value

    def getCell(self, cell: str) -> None:
        if cell[0].isdigit():
            return int(cell)

        row, col = self.cell_to_row(cell)
        return self.sheet[row][col]

    def resetCell(self, cell: str) -> None:
        self.setCell(cell, 0)

    def getValue(self, formula: str) -> int:
        first, second = (formula[1:]).split("+", 2)
        return self.getCell(first) + self.getCell(second)


# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)
