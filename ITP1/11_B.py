def solve():
    class Dice:
        def __init__(self, surface):
            self.Roll = surface

        def S(self):
            self.Roll[0], self.Roll[1], self.Roll[5], self.Roll[4] = self.Roll[4], self.Roll[0], self.Roll[1], self.Roll[5]

        def E(self):
            self.Roll[0], self.Roll[2], self.Roll[5], self.Roll[3] = self.Roll[3], self.Roll[0], self.Roll[2], self.Roll[5]

        def N(self):
            self.Roll[0], self.Roll[4], self.Roll[5], self.Roll[1] = self.Roll[1], self.Roll[0], self.Roll[4], self.Roll[5]

        def W(self):
            self.Roll[0], self.Roll[3], self.Roll[5], self.Roll[2] = self.Roll[2], self.Roll[0], self.Roll[3], self.Roll[5]

    surface = list(map(int, input().split()))
    dice = Dice(surface)
    q = int(input())
    for _ in range(q):
        top,front = map(int, input().split())
        top = dice.Roll.index(top)
        if top == 1:
            dice.N()
        elif top == 2:
            dice.W()
        elif top == 3:
            dice.E()
        elif top == 4:
            dice.S()
        elif top == 5:
            dice.N()
            dice.N()
        
        front = dice.Roll.index(front)
        if front == 1:
            print(dice.Roll[2])
        elif front == 2:
            print(dice.Roll[4])
        elif front == 3:
            print(dice.Roll[1])
        elif front == 4:
            print(dice.Roll[3])

if __name__ == '__main__':
    solve()