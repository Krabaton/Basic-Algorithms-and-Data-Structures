def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0

    while low <= high:

        mid = (high + low) // 2

        # якщо x більше за значення посередині списку, ігноруємо ліву половину
        if arr[mid] < x:
            low = mid + 1

        # якщо x менше за значення посередині списку, ігноруємо праву половину
        elif arr[mid] > x:
            high = mid - 1

        # інакше x присутній на позиції і повертаємо його
        else:
            return mid

    # якщо елемент не знайдений
    return -1


if __name__ == '__main__':
    arr = [2, 3, 4, 10, 40, 50, 60, 70, 80, 90, 100]
    x = 10

    result = binary_search(arr, x)

    if result != -1:
        print("Element is present at index", str(result))
    else:
        print("Element is not present in array")
