
class Node:
    def __init__(self, x):
        self.data = x
        self.next = None


class DNode:
    def __init__(self, x):
        self.data = x
        self.next = None
        self.back = None


class LinkedList:
    def __init__(self):
        self.head = None

    def ins_first(self, x):
        if self.head is None:
            self.head = DNode(x)
            return
        a = DNode(x)
        a.next = self.head
        self.head = a
        a.next.back = a

    def ins_last(self, x):
        if self.head is None:
            self.ins_first()
            return
        c = self.head
        while c.next:
            c = c.next
        a = DNode(x)
        c.next = a
        a.back = c

    def ins_after(self, x, y):
        if self.head is None:
            print("error 0")
            return
        c = self.head
        while c:
            if c.data == x:
                if c.next is None:
                    self.ins_last(y)
                    return
                a = DNode(y)
                a.next = c.next
                c.next = a
                a.next.back = a
                a.back = c
                return
            c = c.next
        print("not found")

    def ins_before(self, x, y):
        if self.head is None:
            print("erorr 0")
            return
        c = self.head
        while c:
            if c.data == x:
                if c.back is None:
                    self.ins_first()
                    return
                temp = DNode(y)
                temp.next = c
                c.back.next = temp
                temp.back = c.back
                c.back = temp
            c.next
        print("x not found")
        return

    def delete_first(self):
        if self.head is None:
            print("error 0")
            return
        # if self.head.next is None:  # tak onsori
        #     del self.head
        #     self.head = None
        #     return
        c = self.head
        self.head = self.head.next  # or c.next
        del c
        if self.head:
            self.head.back = None

    def delete_last(self):
        if self.head is None:
            print("error 0")
            return
        # if self.head.next is None:
        #     self.delete_first()
        #     return
        # c = self.head
        # while c:
        #     if c.next is None:
        #         c.back.next = None
        #         del c
        #         return
        #     c.next
        c = self.head
        while c.next:
            c = c.next
        if c.back is None:
            self.delete_first()
            return
        c.back.next = None
        del c
        return

    def delete_before(self, x):
        if self.head is None:
            print("error 0")
            return
        if self.head.data == x:
            print("error 2")
            return

        c = self.head
        while c:
            if c.data == x:
                a = c.back  # copy of the node we want to delete
                c.back = a.back  # jump over node a
                if a.back:  # if any node before a, jump over a again
                    a.back.next = c
                del a  # delete a
                return
            c = c.next

    def delete_after(self, x):
        if self.head is None:  # empty list
            print("error 0")
            return
        c = self.head
        while c:
            if c.data == x:
                if c.next:
                    a = c.next  # a-> node to be deleted
                    c.next = a.next
                    c.next.back = c
                    if a.next:  # if x is one to last node
                        a.next.back = c
                    del a
                    return
                print("error 1")  # x is last node
                return
            c = c.next
        print("not found")  # x not in list
        return

    def delete_x(self, x):
        if self.head is None:  # empty list
            print("error 0")
            return
        c = self.head
        if self.head.data == x:
            self.delete_first()
            return
        while c:
            if c.data == x:
                if c.next is None:
                    self.delete_last()
                    return
                # self.delete_after(c.back.data)
                c.back.next = c.next
                c.next.back = c.back
                del c
                return
            c = c.next
        print("not found")

    def del_all(self):
        while self.head:
            self.delete_first()
