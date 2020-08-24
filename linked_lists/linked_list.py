class Node:

    def __init__(self, name):
        self.name = name
        self._next = None

    def add_next(self, node):
        self._next = node

    def get_next(self):
        return self._next


if __name__ == '__main__':
    a = Node("A")
    b = Node("B")
    c = Node("C")

    a.add_next(b)
    b.add_next(c)

    current_node = a
    while True:
        next_node = current_node.get_next()
        if not next_node:
            break

        current_node = next_node

    print(current_node.name)
