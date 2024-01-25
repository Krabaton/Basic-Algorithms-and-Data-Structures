import heapq
import random


class Event:
    def __init__(self, order, action):
        self.order = order
        self.action = action

    def __lt__(self, other):
        return self.order < other.order


class Gamer:
    def __init__(self, name, luck):
        self.name = name
        self.luck = luck


gamer = Gamer("Лютий Ярослав", 0.92)

events = [
    Event(1, "Отримав 100 золотих монет"),
    Event(2 - random.randint(3, 5) * gamer.luck, "Отримав меч долі"),
    Event(3 - random.randint(3, 5) * gamer.luck, "Отримав обладунки бога"),
]

heapq.heapify(events)


def simulate_game(events_gamer, gamer_):
    print("Вітаємо, " + gamer.name + "!")
    while events_gamer:
        event = heapq.heappop(events_gamer)
        print(gamer_.name + " " + event.action)


simulate_game(events, gamer)
