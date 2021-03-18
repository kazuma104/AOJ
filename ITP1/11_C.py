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

        def shift(self):
            self.Roll[1], self.Roll[2], self.Roll[3], self.Roll[4], self.Roll[5], self.Roll[0] = self.Roll[0], self.Roll[1], self.Roll[2], self.Roll[3], self.Roll[4], self.Roll[5]

    surface = list(map(int, input().split()))
    dice1 = Dice(surface)
    surface = list(map(int, input().split()))
    dice2 = Dice(surface)
    flag = False
    if set(dice1.Roll) == set(dice2.Roll):
        top = dice2.Roll.index(dice1.Roll[0])
        if top == 1:
            dice2.N()
        elif top == 2:
            dice2.W()
        elif top == 3:
            dice2.E()
        elif top == 4:
            dice2.S()
        elif top == 5:
            dice2.N()
            dice2.N()
        
        front = dice2.Roll.index(dice1.Roll[1])
        if front == 2:
            dice2.W()
            dice2.S()
            dice2.E()
        elif front == 3:
            dice2.E()
            dice2.S()
            dice2.W()
        elif front == 4:
            dice2.E()
            dice2.N()
            dice2.N()
            dice2.W()
        for _ in range(6):
            if dice1.Roll == dice2.Roll:
                flag = True
            dice2.shift()
        else:
            pass
    else:
        pass
    print("Yes" if flag else "No")

if __name__ == '__main__':
    solve()