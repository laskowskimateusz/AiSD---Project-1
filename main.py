from Stack import *
from Queue import *


def test_linked_list():
    list_ = LinkedList()
    assert list_.head is None
    list_.push(1)
    list_.push(0)

    assert str(list_) == '0 -> 1'
    list_.append(9)
    list_.append(10)

    assert str(list_) == '0 -> 1 -> 9 -> 10'
    middle_node = list_.node(at=1)
    list_.insert(5, after=middle_node)

    assert str(list_) == '0 -> 1 -> 5 -> 9 -> 10'
    first_element = list_.node(at=0)
    returned_first_element = list_.pop()

    assert first_element.value == returned_first_element

    last_element = list_.node(at=3)
    returned_last_element = list_.remove_last()

    assert last_element.value == returned_last_element
    assert str(list_) == '1 -> 5 -> 9'

    second_node = list_.node(at=1)
    list_.remove(second_node)

    assert str(list_) == '1 -> 5'


def test_stack():
    stack = Stack()

    assert len(stack) == 0

    stack.push(3)
    stack.push(10)
    stack.push(1)

    assert len(stack) == 3

    top_value = stack.pop()

    assert top_value == 1

    assert len(stack) == 2


def test_queue():
    queue = Queue()

    assert len(queue) == 0

    queue.enqueue('klient1')
    queue.enqueue('klient2')
    queue.enqueue('klient3')

    assert str(queue) == 'klient1, klient2, klient3'

    client_first = queue.dequeue()

    assert client_first == 'klient1'
    assert str(queue) == 'klient2, klient3'
    assert len(queue) == 2


if __name__ == '__main__':
    test_linked_list()
    test_stack()
    test_queue()
