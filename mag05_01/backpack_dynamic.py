def knap_sack(W, wt, val, n):
    # створюємо таблицю K для зберігання оптимальних значень підзадач
    K = [[0 for w in range(W + 1)] for i in range(n + 1)]

    # будуємо таблицю K знизу вгору
    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif wt[i - 1] <= w:
                K[i][w] = max(val[i - 1] + K[i - 1][w - wt[i - 1]], K[i - 1][w])
            else:
                K[i][w] = K[i - 1][w]

    for el in K:
        print(el)
    return K[n][W]


if __name__ == "__main__":
    # ваги та вартість предметів
    value = [60, 100, 120]
    weight = [10, 20, 30]
    # місткість рюкзака
    capacity = 50
    # кількість предметів
    n = len(value)
    # виклик функції
    print(knap_sack(capacity, weight, value, n))  # 220
