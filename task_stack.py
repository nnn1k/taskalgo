class my_stack:

    def __init__(self):
        self.stack = []

    def push(self, el):
        self.stack.append(el)

    def pop(self):
        return self.stack.pop()

    def size(self):
        return len(self.stack)

def test_1():
    s = my_stack()
    s.push(1)
    assert s.pop() == 1


test_1()


def test_2():
    s = my_stack()
    s.push(1)
    assert s.size() == 1


test_2()


def test_3():
    s = my_stack()
    s.push(1)
    s.push(2)
    s.pop()
    s.push(3)
    s.push(4)
    assert s.pop() == 4
    assert s.size() == 2
    assert s.pop() == 3


test_3()