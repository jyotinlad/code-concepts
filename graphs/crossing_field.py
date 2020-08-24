from copy import deepcopy


class FieldCrossing:

    def __init__(self, field):
        self.field = field

        self._max_x = len(self.field[0]) - 1
        self._max_y = len(self.field) - 1
        self._moves = [(0, -1), (1, 0), (0, 1), (-1, 0)]

    def _check_sensor(self, coord):
        return False if self.field[coord[1]][coord[0]] else True

    def _get_moves(self, coord, visited):
        x = coord[0]
        y = coord[1]

        moves = []
        for move in self._moves:
            new_x = x + move[0]
            new_y = y + move[1]
            if new_x < 0 or new_x > self._max_x or new_y < 0 or new_y > self._max_y:
                continue

            if visited[new_y][new_x]:
                continue

            # check if sensor
            if self._check_sensor((new_x, new_y)):
                continue

            visited[new_y][new_x] = True
            moves.append(move)

        return moves

    def get_shortest_crossing(self):
        counts = []

        for y, row in enumerate(self.field):
            start = (0, y)

            # check if sensor
            if self._check_sensor((0, y)):
                continue

            # TODO use python in built queues
            queue = [[]]

            visited = [[None for _ in x] for x in self.field]

            print(f"starting at position: {start}")
            while True:
                if not queue:
                    break

                x = start[0]
                y = start[1]

                route = queue.pop(0)

                # start moving through field
                for move in route:
                    x += move[0]
                    y += move[1]

                # made it to end of field
                if x == self._max_x:
                    counts.append(len(route))
                    break

                # explore new routes
                current_pos = (x, y)
                for move in self._get_moves(current_pos, visited):
                    new_route = deepcopy(route)
                    new_route.append(move)
                    queue.append(new_route)

        return min(counts)


if __name__ == '__main__':
    field = [
        [0, 1, 0, 1, 0, 1, 1, 1, 1, 1],
        [1, 1, 0, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 0, 1, 1, 1, 1, 1, 0, 1],
        [1, 1, 0, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 0, 1, 1, 0, 1, 1, 1, 1],
        [1, 1, 0, 1, 1, 1, 0, 1, 1, 1],
        [1, 1, 1, 1, 0, 1, 1, 0, 1, 0],
        [1, 1, 0, 1, 1, 1, 1, 1, 1, 0],
        [1, 1, 0, 1, 1, 0, 1, 1, 1, 0],
        [1, 1, 0, 1, 1, 1, 1, 1, 1, 1]
    ]

    fc = FieldCrossing(field)
    length = fc.get_shortest_crossing()

    message = f"shortest crossing {length}" if length else "no crossing possible"
    print(message)
