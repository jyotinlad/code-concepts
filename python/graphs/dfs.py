data = [
    [1, 1, 0, 0],
    [0, 1, 1, 0],
    [0, 0, 1, 0],
    [1, 0, 0, 0]
]

class Coord:

    def __init__(self, x, y):
        self.x = x
        self.y = y

def _find_next(coord, grid, visited):
    print(f"working from {coord}")
    visited.append(coord)

    x, y = coord
    max_x = len(grid[y]) - 1
    max_y = len(grid) - 1

    # analyse right
    if x < max_x:
        x += 1
        value = grid[y][x]
        new_coord = (x, y)
        if value and new_coord not in visited:
            _find_next(new_coord, grid, visited)

    top_range_max = 2 if coord[0] == 0 or coord[0] == max_x else 3

    # analyse bottom row
    if y < max_y:
        # start diagonal right
        y += 1
        for i in range(x, x-top_range_max, -1):
            x = i
            value = grid[y][x]
            new_coord = (x, y)
            if value and new_coord not in visited:
                _find_next(new_coord, grid, visited)

    # analyse left
    x = coord[0]
    if x > 0:
        x = coord[0] - 1
        y = coord[1]
        value = grid[y][x]
        new_coord = (x, y)
        if value and new_coord not in visited:
            _find_next(new_coord, grid, visited)

    # analyse top
    if coord[1] > 0:
        y = coord[1] - 1
        for i in range(x, x+top_range_max):
            x = i
            value = grid[y][x]
            new_coord = (x, y)
            if value and new_coord not in visited:
                _find_next(new_coord, grid, visited)

    return len(visited)


def max_grid(grid):
    routes = []
    for y, row in enumerate(grid):
        for x, value in enumerate(row):
            coord = (x, y)
            if value:
                print(f"starting route")
                connections = _find_next(coord, grid, [])
                routes.append(connections)

    return max(routes)


if __name__ == "__main__":
    print(max_grid(data))