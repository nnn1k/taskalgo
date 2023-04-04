class MiracleList():
    data: []
    el: 0

    def __init__(self, data):
        self.data = data

    def get_data(self):
        return self.data

    def sort(self):
        for i in range(len(self.data)-1):
            for j in range(len(self.data)-i-1):
                if self.data[j] > self.data[j+1]:
                    self.data[j], self.data[j+1] = self.data[j+1], self.data[j]

    def bin(self, el):
        l = -1
        r = len(self.data)
        while l < r:
            mid = (l + r) // 2
            if self.data[mid] > el:
                r = mid
            elif el == self.data[mid]:
                return mid + 1
                break
            else:
                l = mid



def test_get_data():
    ml = MiracleList([1, 2, 3])
    assert ml.get_data() == [1, 2, 3]


def test_sort():
    ml = MiracleList([2, 3, 1])
    ml.sort()
    assert ml.get_data() == [1, 2, 3]


def test_bin():
    ml = MiracleList([2, 3, 1])
    ml.sort()
    assert ml.bin(1) == 1

ml = MiracleList([1, 2, 3])
test_get_data()
test_sort()
test_bin()
