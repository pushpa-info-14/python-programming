class Spreadsheet:
    def __init__(self, rows: int):
        self._cells = {}

    def setCell(self, cell: str, value: int) -> None:
        self._cells[cell] = value

    def resetCell(self, cell: str) -> None:
        if cell in self._cells:
            del self._cells[cell]

    def getValue(self, formula: str) -> int:
        x, y = formula[1:].split("+")
        a = self._cells.get(x, 0) if x[0].isalpha() else int(x)
        b = self._cells.get(y, 0) if y[0].isalpha() else int(y)
        return a + b