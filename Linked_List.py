class Node:
    def __init__(self, d):
        self.data = d
        self.next = None


# insert types: after, before, last, first
# delete types: first, last, after, before, x, all
class LinkedList:
    def __init__(self):
        self.head = None

    def insert_first(self, x):
        if self.head is None:
            self.head = Node(x)

    def insert_last(self, x):
        if self.head is None:
            self.head = Node(x)
        else:
            a = Node(x)
            c = self.head
            while c.next:
                c = c.next
            c.next = a

    def insert_after(self, x, y):  # add y after x
        # bugs: 1.always print not found without the return on the loop. 2.if x=y the loop never ends
        # bug 2 is solved with a flag, the flag is set to true if any node.next is set
        inserted_any = False
        if self.head is None:  # list empty
            print("list is empty")
        else:
            # we shouldn't touch head, so we copy head
            c = self.head
            while c:
                if c.data == x:
                    a = Node(y)
                    a.next = c.next
                    c.next = a
                    c = c.next
                    inserted_any = True
                    return  # return if you want to insert y after all the x in list
                c = c.next
            if not inserted_any:
                print("x not found")

    def insert_before(self, x, y):
        if self.head is None:
            print("list is empty")
        if self.head.data == x:
            self.insert_first(y)
            return
        c = self.head
        while c.next:
            if c.next.data == x:
                a = Node(y)
                a.next = c.next
                c.next = a
                c = c.next

    def delete_first(self):  # exceptions: emptiness(head=None),
        if self.head is None:
            print("error 0")
            return
        # 1. copy head 2. move head 3. free memory
        c = self.head
        self.head = c.next
        del c

    def delete_last(self):  # exceptions: 1.emptiness 2.only one element
        if self.head is None:
            print("error 0")
            return
        if self.head.next is None:  # only one element in list
            self.delete_first()
            return
        # 1. copy head 2.move to one to last(not last) 3.free last node 4.one-to-last.next = None
        c = self.head  # 1
        while c.next.next:  # 2
            # move to one to last element
            c = c.next
        del c.next  # 3
        c.next = None  # 4

    def delete_after(self, x):
        # exceptions: emptiness, only one element, x last element, x not in list
        if self.head is None:
            print("error 0")
            return
        if self.head.next is None:  # only one element in list
            print("error 1")
            return
        # copy, jump, delete
        c = self.head
        while c.next.next:
            if c.data == x:
                a = c.next
                c.next = a.next
                del a
                return
            c = c.next
        print("not found")

    def delete_before(self, x):
        # exceptions: emtpiness, one element, two element, x not in list
        if self.head is None:  # list empty
            print("error 0")
            return
        if self.haed.data == x:  # x doesnt have a before
            print("error x1")
            return
        if self.head.next is None:  # one element only
            print("error 1")
            return
        if self.head.next.data == x:  # x is second element
            self.delete_first()
            return
        if self.head.next.next is None:  # only two elements in list without x
            print("error 2")
            return
        c = self.head
        while c.next.next:
            if c.next.next.data == x:
                a = c.next
                c.next = a.next
                del a
                return
            c = c.next
        print("not found")  # x not in list

    def delete_all(self):
        while self.head:
            self.delete_first()

    def delete_x(self, x):
        # exceptions: x not in list,
        if self.head is None:
            print("error 0")
            return
        if self.head.data == x:
            self.delete_first()
            return
        c = self.head
        while c.next:
            if c.next.data == x:
                a = c.next
                c.next = a.next
                del a
                return
            c = c.next
        print("not found")