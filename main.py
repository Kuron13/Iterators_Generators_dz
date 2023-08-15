import types
class FlatIterator:

    def __init__(self, list_of_list):
        self.data_list = list_of_list

    def __iter__(self):
        self.i = -1
        self.sub_i = -1
        self.sub_list = []
        self.item = []
        return self

    def __next__(self):
        if len(self.sub_list) == 0:
            self.i += 1
            if self.i >= len(self.data_list):
                raise StopIteration
            self.sub_list = self.data_list[self.i]
        self.sub_i += 1
        if self.sub_i < len(self.sub_list):
            self.item = self.sub_list[self.sub_i]
            if self.sub_i == len(self.sub_list)-1:
                self.sub_list = []
                self.sub_i = -1
        return self.item

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



def flat_generator(list_of_lists):
    for i in list_of_lists:
        for sub_i in i:
            yield sub_i

def test_2():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

    assert isinstance(flat_generator(list_of_lists_1), types.GeneratorType)

if __name__ == '__main__':
    test_1()

    # for item in FlatIterator(list_of_list=[
    #     ['a', 'b', 'c'],
    #     ['d', 'e', 'f', 'h', False],
    #     [1, 2, None]
    # ]):
    #     print(item)

    test_2()

    # for item in flat_generator(list_of_lists=[
    #     ['a', 'b', 'c'],
    #     ['d', 'e', 'f', 'h', False],
    #     [1, 2, None]
    # ]):
    #     print(item)


