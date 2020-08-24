def merge_sort(arr):
    if not len(arr) > 1:
        return arr

    middle = int(len(arr) / 2)
    print(middle)

    left = arr[:middle]
    right = arr[middle:]
    print(left)
    print(right)

    left = merge_sort(left)
    right = merge_sort(right)

    new_arr = []
    while True:
        if not left:
            new_arr.extend(right)
            break

        if not right:
            new_arr.extend(left)
            break

        if left[0] <= right[0]:
            new_arr.append(left.pop(0))
        elif right[0] < left[0]:
            new_arr.append(right.pop(0))

    print("sorted", new_arr)
    return new_arr


def merge():
    pass


def run(arr):
    return merge_sort(arr)


if __name__ == '__main__':
    values = [20, 3, 5, 18, 10, 7, 2]

    print(run(values))
