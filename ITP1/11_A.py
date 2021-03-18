def solve():
    class Dice:
        def __init__(self, surface):
            self.surface = surface

    surface = list(map(int, input().split()))
    dice = Dice(surface)

    print(dice.surface)

if __name__ == '__main__':
    solve()