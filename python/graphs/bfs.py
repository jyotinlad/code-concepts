from pprint import PrettyPrinter
from copy import deepcopy


def is_valid(coord, move, x, y):
	new_x = coord[0] + move[0]
	new_y = coord[1] + move[1]
	if new_x < 0 or new_x > x or new_y < 0 or new_y > y:
		return False

	return True


def calc_distance(coord, matrix):
	print(f"starting at {coord}")
	max_x = len(matrix[0]) - 1
	max_y = len(matrix) - 1

	queue = []
	queue.append([])

	while queue:
		path = queue.pop(0)
		if path:
			print(path)
			x = coord[0]
			y = coord[1]
			for move in path:
				x += move[0]
				y += move[1]

			value = matrix[y][x]
			if value == "M":
				# mine
				print("mine", path, x, y)
				return len(path)
			elif value == "X":
				print("blocked", path, x, y)
				continue

		# TODO move into function
		# get valid moves
		moves = [(0, -1), (1, 0), (0, 1), (-1, 0)]
		for move in moves:
			if not is_valid(coord, move, max_x, max_y):
				continue
			new_path = deepcopy(path)
			new_path.append(move)
			queue.append(new_path)

		# explore options
		# exit()

	return 99  # TODO fix


def get_value(coord, matrix):
	value = matrix[coord[1]][coord[0]]
	if value == "M":
		return 0
	elif value == "X":
		return -1
	else:
		return calc_distance(coord, matrix)


def explore(matrix):
	get_value((4, 4), matrix)
	mapped = []
	for row_id, row in enumerate(data):
		mapped.append([None for _ in row])
		for i, value in enumerate(row):
			mapped[row_id][i] = get_value((i, row_id), matrix)

	return mapped



if __name__ == '__main__':
	data = [
		['O', 'M', 'O', 'O', 'X'],
		['O', 'X', 'X', 'O', 'M'],
		['O', 'O', 'O', 'O', 'O'],
		['O', 'X', 'X', 'X', 'O'],
		['O', 'O', 'M', 'O', 'O'],
		['O', 'X', 'X', 'M', 'O']
	]

	pp = PrettyPrinter()
	pp.pprint(explore(data))
