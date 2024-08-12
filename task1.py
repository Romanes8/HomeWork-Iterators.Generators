#Задание №1
class FlatIterator:
    def __init__(self, list_of_list):
        self.main_list = list_of_list

    def __iter__(self):
        self.main_index = 0
        self.inner_index = -1
        return self

    def __next__(self):
        self.inner_index += 1
        if self.inner_index == len(self.main_list[self.main_index]):
            self.main_index += 1
            self.inner_index = 0
        if self.main_index == len(self.main_list):
            raise StopIteration
        return self.main_list[self.main_index][self.inner_index]


def test_1():
    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):
        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()
