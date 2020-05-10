from collections import deque

if __name__ == "__main__":
    dlist = input().split()
    result = deque()
    for p in dlist:
        if p in"+-*": #["+","-","*"]でも可
            hen1 = result.pop()
            hen2 = result.pop()
            result.append(str(eval(hen2 + p + hen1)))
        else:
            result.append(p)  
        #print(result)
    print(result.pop())