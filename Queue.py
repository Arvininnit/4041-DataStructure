class Queue:
    def __init__(self, max=100):
        self.list = [None] * max  # static queue with predetermined length, not dynamic
        # if queue was empty, by convention we put front and rear to -1
        self.front = -1  # empty queue
        self.rear = -1  # empty queue

    def insert(self, x):
        if self.rear >= len(self.list) - 1:  # when queue is full
            print("Queue is Full!")
            return
        if self.front == -1:  # when queue is empty
            self.front += 1
            self.rear += 1
            self.list[self.rear] = x
            return
        # when regular situation
        self.rear += 1
        self.list[self.rear] = x

    def delete(self):
        if self.front == -1:  # when queue empty
            print("Queue is empty!")
            return
        if self.front == self.rear:  # when only one element in queue
            k = self.list[self.front]
            self.front = -1
            self.rear = -1
            return k
        # regular situation
        k = self.list(self.front)
        self.front += 1
        return k


# پر شدن مجازی
# this queue has the problem of : virtual fullness
# which means unless the whole queue gets empty again, we cannot insert any element to it
# it can be fixed with shifting every element to left after we pop an element from the front

# با ساختمان داده حلقوی حل میشود