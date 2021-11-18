from LinkedList import *


class Stack:
    _storage: LinkedList

    def __init__(self):
        self._storage = LinkedList()

    def push(self, element: Any) -> None:
        self._storage.append(element)

    def pop(self) -> Any:
        return self._storage.remove_last()

    def __len__(self) -> int:
        return len(self._storage)

    def __str__(self):
        string: str = ''
        loop = len(self) - 1
        while loop >= 0:
            string += str(self._storage.node(loop).value) + '\n'
            loop -= 1
        return string
