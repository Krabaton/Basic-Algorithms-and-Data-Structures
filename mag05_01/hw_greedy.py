coins = [50, 25, 10, 5, 2, 1]


def find_coins_greedy(sum_: int):
    count_coins = {}
    for coin in coins:
        count = sum_ // coin
        if count > 0:
            count_coins[coin] = count
        sum_ = sum_ - coin * count
    return count_coins


if __name__ == "__main__":
    result = find_coins_greedy(87)
    print(result)
