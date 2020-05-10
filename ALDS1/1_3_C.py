from collections import deque

if __name__ == "__main__":
    n = int(input())
    command =[input() for x in range(n)]
    DLList = deque()
    for c in command:
        if c[0] == "i":
            DLList.appendleft(c[7:])
        elif c[6] == " ":
            if c[7:] in DLList:
                DLList.remove(c[7:])
        elif c[6] == "F":
            DLList.popleft()
        else:
            DLList.pop()

    print(*DLList)