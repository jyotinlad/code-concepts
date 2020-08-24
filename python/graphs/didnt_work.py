from copy import deepcopy
from sys import exit


class IslandAnalyser:

    def __init__(self, matrix):
        # TODO check valid matrix?
        self.matrix = matrix
        self._max_x = len(self.matrix[0]) - 1
        self._max_y = len(self.matrix) - 1

        self._moves = [(0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1)]

    def _is_land(self, x, y):
        return True if self.matrix[y][x] else False

    def _get_valid_moves(self, coord, visited):
        x = coord[0]
        y = coord[1]

        moves = []
        for move in self._moves:
            new_x = x + move[0]
            new_y = y + move[1]

            # check in matrix/grid
            if new_x < 0 or new_x > self._max_x or new_y < 0 or new_y > self._max_y:
                continue

            # check not visited
            if visited[new_y][new_x]:
                continue

            # check is land
            if not self._is_land(new_x, new_y):
                continue

            visited[new_y][new_x] = True
            moves.append(move)

        return moves

    def _get_land_points(self):
        points = []
        for y, row in enumerate(self.matrix):
            for x, value in enumerate(self.matrix[y]):
                coord = (x, y)

                # check if land
                if not self._is_land(x, y):
                    continue

                points.append(coord)

        return points

    def get_islands(self):
        # to process all the routes to take
        queue = []

        # visited nodes
        visited = [[False for x in y] for y in self.matrix]

        islands = 0
        for coord in self._get_land_points():
            print(f"starting point: {coord}")

            if visited[coord[1]][coord[0]]:
                continue

            # add to visited land
            visited[coord[1]][coord[0]] = True

            queue.append([])

            counter = 0
            while True:
                counter += 1
                if counter == 8:
                    # exit()
                    pass

                new_x = coord[0]
                new_y = coord[1]
                route = queue.pop(0)
                print("route", route)

                # start moving
                for move in route:
                    new_x += move[0]
                    new_y += move[1]

                new_coord = (new_x, new_y)
                print("new coord", new_coord)
                moves = self._get_valid_moves(new_coord, visited)
                if not moves:
                    break

                for move in moves:
                    new_route = deepcopy(route)
                    new_route.append(move)
                    queue.append(new_route)
                    print("new route", new_route)

            islands += 1

        return islands


if __name__ == '__main__':
    mat = [
        [1, 0, 1, 0, 0, 0, 1, 1, 1, 1],
        [0, 0, 1, 0, 1, 0, 1, 0, 0, 0],
        [1, 1, 1, 1, 0, 0, 1, 0, 0, 0],
        [1, 0, 0, 1, 0, 1, 0, 0, 0, 0],
        [1, 1, 1, 1, 0, 0, 0, 1, 1, 1],
        [0, 1, 0, 1, 0, 0, 1, 1, 1, 1],
        [0, 0, 0, 0, 0, 1, 1, 1, 0, 0],
        [0, 0, 0, 1, 0, 0, 1, 1, 1, 0],
        [1, 0, 1, 0, 1, 0, 0, 1, 0, 0],
        [1, 1, 1, 1, 0, 0, 0, 1, 1, 1]
    ]

    analyser = IslandAnalyser(mat)
    print(analyser.get_islands())
