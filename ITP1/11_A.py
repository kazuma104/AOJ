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
    D = input()
    for d in D:
        if d == "S":
            dice.S()
        elif d == "E":
            dice.E()
        elif d == "N":
            dice.N()
        elif d == "W":
            dice.W()

    print(dice.Roll[0])

if __name__ == '__main__':
    solve()