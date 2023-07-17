import heapq
from dataclasses import dataclass


@dataclass
class Item:
    key: int
    value: int

    def __lt__(self, other: "Item"):
        return self.key < other.key


class Heap:
    def __init__(self) -> None:
        self.__data: list[Item] = []

    def push(self, item: Item) -> None:
        heapq.heappush(self.__data, item)

    def pop(self) -> Item:
        return heapq.heappop(self.__data)

    def __repr__(self) -> str:
        return str(self.__data)


class Stack:
    def __init__(self) -> None:
        self.heap = Heap()
        self.current_key = 0

    def push(self, item: int) -> None:
        # the heapq module supports max heaps buts it a lil sus and undocumented
        # so instead of using that im just negating the key
        # this will make the most recent item at the top of the heap
        self.heap.push(Item(self.current_key * -1, item))
        self.current_key += 1

    def pop(self) -> int:
        item = self.heap.pop()
        return item.value


s = Stack()

s.push(5)
s.push(7)
s.push(10)
s.push(2)
s.push(12)

assert s.pop() == 12
assert s.pop() == 2
assert s.pop() == 10
assert s.pop() == 7
assert s.pop() == 5
