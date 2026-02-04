class Stack:
    def __init__(self, is_dynamic=True, limit=10):
        self.limit = limit
        if is_dynamic:
            self.dynamic = True
            self.stack = []
        else:
            self.dynamic = False
            self.stack = [None] * limit

    def convert_to_dynamic(self):
        if not self.dynamic:
            new_stack = []
            for elem in self.stack:
                new_stack.append(elem)
            self.stack = new_stack
            self.dynamic = True
        else:
            print("Already Dynamic!")
            return -1

    def convert_to_static(self, limit=10):
        if self.dynamic:
            new_stack = [None] * self.limit
            for i in range(len(self.stack)):
                new_stack[i] = self.stack[i]
            self.stack = new_stack
            self.dynamic = False
        else:
            print("Already Static!")
            return -1

    def push(self, data):
        if self.dynamic:
            if self.size() >= self.limit:
                print("Stack is Full!")
                return -1
            self.stack.append(data)
        else:
            if self.size() >= self.limit:
                print("Stack is Full!")
                return -1
            self.stack[self.size() + 1] = data

    def pop(self):
        if len(self.stack) == 0:
            return -1
        return self.stack.pop()

    def peek(self):
        if len(self.stack) <= 0:
            return -1
        return self.stack[-1]

    def show(self):
        return self.stack

    def display(self):
        for i in reversed(self.stack):
            print(i)

    def replace(self, old, new):
        for i in range(len(self.stack)):
            if self.stack[i] == old:
                self.stack[i] = new
                return True
        return False

    def find(self, value):
        return value in self.stack

    def size(self):
        if not self.dynamic:
            size = 0
            for elem in self.stack:
                if elem is not None:
                    size += 1
            return size
        else:
            return len(self.stack)


if __name__ == "__main__":
    s = Stack(is_dynamic=True, limit=12)