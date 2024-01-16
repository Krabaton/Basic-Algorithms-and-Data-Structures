def interpolation_search(arr, x):
    low = 0
    high = len(arr) - 1

    while low <= high and arr[low] <= x <= arr[high]:
        index = low + int(((float(high - low) / (arr[high] - arr[low])) * (x - arr[low])))
        if arr[index] == x:
            return index
        if arr[index] < x:
            low = index + 1
        else:
            high = index - 1

    return -1


if __name__ == '__main__':
    arr = [2, 3, 4, 10, 40, 50, 60, 70, 80, 90, 100]
    x = 60

    result = interpolation_search(arr, x)

    if result != -1:
        print("Element is present at index", str(result))
    else:
        print("Element is not present in array")
