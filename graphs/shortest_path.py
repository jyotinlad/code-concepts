from copy import deepcopy


class MazeExplorer:

    def __init__(self, grid):
        # TODO validate grid
        self.grid = grid
        self._max_x = len(grid[0]) - 1
        self._max_y = len(grid) - 1

        self._moves = [(0, -1), (1, 0), (0, 1), (-1, 0)]

    def _valid_moves(self, coord, visited):
        x = coord[0]
        y = coord[1]

        valid = []
        for move in self._moves:
            new_x = x + move[0]
            new_y = y + move[1]
            if new_x < 0 or new_x > self._max_x or new_y < 0 or new_y > self._max_y:
                continue

            # # check new location == 1
            if not self.grid[new_y][new_x] or visited[new_y][new_x]:
                continue

            valid.append(move)

        return valid

    def get_shortest_path(self, start, end):
        queue = [[]]

        # TODO check start is valid

        visited = [[False for _ in range(self._max_x + 1)] for _ in range(self._max_y + 1)]

        while queue:
            x = start[0]
            y = start[1]

            route = queue.pop(0)

            # move to new position
            for move in route:
                x += move[0]
                y += move[1]

            visited[y][x] = True

            # # check new location == 1
            # if not self.grid[y][x]:
            #     continue

            # check if at end
            if x == end[0] and y == end[1]:
                return len(route)

            # add new moves to route
            new_coord = (x, y)
            for move in self._valid_moves(new_coord, visited):
                new_route = deepcopy(route)
                new_route.append(move)
                queue.append(new_route)

        return 0


if __name__ == '__main__':
    maze = [
        [1, 1, 1, 1, 1, 0, 0, 1, 1, 1],
        [0, 1, 1, 1, 1, 1, 0, 1, 0, 1],
        [0, 0, 1, 0, 1, 1, 1, 0, 0, 1],
        [1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
        [0, 0, 0, 1, 0, 0, 0, 1, 0, 1],
        [1, 0, 1, 1, 1, 0, 0, 1, 1, 0],
        [0, 0, 0, 0, 1, 0, 0, 1, 0, 1],
        [0, 1, 1, 1, 1, 1, 1, 1, 0, 0],
        [1, 1, 1, 1, 1, 0, 0, 1, 1, 1],
        [0, 0, 1, 0, 0, 1, 1, 0, 0, 1]
    ]

    # find shortest path from source (0, 0) to destination (7, 5) = 12
    explorer = MazeExplorer(maze)
    value = explorer.get_shortest_path((0, 0), (7, 5))

    print(value)
