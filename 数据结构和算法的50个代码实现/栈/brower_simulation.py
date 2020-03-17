class Brower:
    """
    模拟浏览器后退和前进
    """
    def __init__(self):
        self.prev = []
        self.next = []

    def open(self, url):
        self.prev.append(url)

    def forward(self):
        if not self.next:
            return -1
        self.prev.append(self.next.pop())
        return self.prev[-1]

    def back(self):
        if not self.prev:
            return -1
        self.next.append(self.prev.pop())
        return self.next[-1]


if __name__ == '__main__':
    brower = Brower()
    brower.open('a')
    brower.open('b')
    brower.open('c')
    brower.back()
    brower.forward()
    brower.forward()
