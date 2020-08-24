class Flood:

    def __init__(self, matrix):
        # TODO test valid matrix
        self.matrix = matrix

        self._max_y = len(self.matrix) - 1
        self._max_x = len(self.matrix[0]) - 1

        # TODO configurable
        self._moves = [(0, -1), (1, 0), (0, 1), (-1, 0)]
        self._counts = []

    def _valid_moves(self, x, y):
        valid = []
        for move in self._moves:
            if x + move[0] < 0 or x + move[0] > self._max_x or y + move[1] < 0 or y + move[1] > self._max_y:
                continue

            valid.append(move)

        return valid

    def _traverse_path(self, x, y, visited):
        value = self.matrix[x][y]
        visited.append((x, y))

        for move in self._valid_moves(x, y):
            new_coord = (x + move[0], y + move[1])
            new_value = self.matrix[new_coord[0]][new_coord[1]]
            if new_value != value or new_coord in visited:
                self._counts.append(len(visited))
                continue

            self._traverse_path(new_coord[0], new_coord[1], visited)

    def calculate(self):
        print("starting..")

        for y, row in enumerate(self.matrix):
            for x, value in enumerate(row):
                self._traverse_path(x, y, [])

        return max(self._counts)


if __name__ == "__main__":
    M = [
        ['Y', 'Y', 'Y', 'G', 'G', 'G', 'G', 'G', 'G', 'G'],
        ['Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'G', 'X', 'X', 'X'],
        ['G', 'G', 'G', 'G', 'G', 'G', 'G', 'X', 'X', 'X'],
        ['W', 'W', 'W', 'W', 'W', 'G', 'G', 'G', 'G', 'X'],
        ['W', 'R', 'R', 'R', 'R', 'R', 'G', 'X', 'X', 'X'],
        ['W', 'W', 'W', 'R', 'R', 'G', 'G', 'X', 'X', 'X'],
        ['W', 'B', 'W', 'R', 'R', 'R', 'R', 'R', 'R', 'X'],
        ['W', 'B', 'B', 'B', 'B', 'R', 'R', 'X', 'X', 'X'],
        ['W', 'B', 'B', 'X', 'B', 'B', 'B', 'B', 'X', 'X'],
        ['W', 'B', 'B', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
    ]

    flood = Flood(M)
    print(flood.calculate())
