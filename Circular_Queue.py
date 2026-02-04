class Circular_Queue:
    def __init__(self, max):
        self.list = [None] * max
        self.front = -1
        self.rear = -1

    def ins(self, x):
        if (self.rear + 1) % len(self.list) == self.front:  # cq is full
            print("CQ is full")
            return
        if self.front == -1:  # cq is empty
            self.front = 0
            self.rear = 0
            self.list[self.rear] = x
        # regular situation
        self.rear += (self.rear) % len(
            self.list
        )  # we should now immidiately calculare % max to make cq circular
        self.list[self.rear] = x

    def delete(self):
        if self.front == -1:
            print("CQ is Empty")
            return
        if self.front == self.rear:
            k = self.list[self.front]
            self.rear = -1
            return k
        k = self.list[self.rear]
        self.front = (self.front + 1) % len(self.list)

    def is_full(self):
        return (self.rear + 1) % len(self.list) == 1

    def is_empty(self):
        return self.front == -1


# isfull, isempty, showvalid, showinvalid, find, replace