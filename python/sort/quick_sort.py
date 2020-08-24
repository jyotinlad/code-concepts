def partition(arr, start, end):
    pivot = arr[start]
    low = start + 1
    high = end

    while True:
        while low <= high and arr[high] >= pivot:
            high -= 1

        while low <= high and arr[low] <= pivot:
            low += 1

        if low <= high:
            arr[low], arr[high] = arr[high], arr[low]
        else:
            break

    arr[start], arr[high] = arr[high], arr[start]

    return high


def quick_sort(arr, start, end):
    if start >= end:
        return

    pi = partition(arr, start, end)
    quick_sort(arr, start, pi - 1)
    quick_sort(arr, pi + 1, end)


def run(arr):
    return quick_sort(arr, 0, len(arr) - 1)


if __name__ == '__main__':
    values = [20, 3, 5, 18, 10, 7, 2]

    run(values)
    print(values)
