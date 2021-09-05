s = []


def push():
    item = int(input("Enter item to be pushed:"))
    s.append(item)


def pop():
    print(s.pop())


def display():
    print("Elements in stack are:", s)


def exit1():
    quit()


def menu(i):
    switch = {
        1: push,
        2: pop,
        3: display,
        4: exit1
    }
    func = switch.get(i, "Invalid choice")
    return func()


while(1):
    print("Stack Program")
    print("1.Push\n2.Pop\n3.Display Stack\n4.Exit")
    ch = int(input("Enter your choice:"))
    menu(ch)
