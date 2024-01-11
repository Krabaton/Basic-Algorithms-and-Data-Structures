def counting_sort(arr, position):
    size = len(arr)
    output = [0] * size
    count = [0] * 10

    # Рахунок входжень певного розряду
    for i in range(0, size):
        index = arr[i] // position % 10
        count[index] += 1

    # Оновлення count[i] так, щоб він показував позицію наступного входження своєї цифри
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Побудова вихідного масиву
    i = size - 1
    while i >= 0:
        index = arr[i] // position % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1
        i -= 1

    for i in range(0, size):
        arr[i] = output[i]


def radix_sort(arr):
    # Визначення максимального числа для визначення кількості розрядів
    max_num = max(arr)
    position = 1
    # Виконання counting_sort для кожного розряду
    while max_num // position > 0:
        counting_sort(arr, position)
        position *= 10


if __name__ == '__main__':
    arr = [3, 89, 67, 254, 9, 21, 185, 4, 62]
    radix_sort(arr)
    print("Відсортований масив:", arr)  # Відсортований масив: [3, 4, 9, 21, 62, 67, 89, 185, 254]
