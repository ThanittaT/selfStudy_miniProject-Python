class Duck:
    sound = 'Quaack!'
    walking = "Walking like a duck!"

    def quack(self):
        # print('Quaack!')
        print(self.sound)

    def walk(self):
        # print('Walking like a duck.!')
        print(self.walking)


def main():
    donald = Duck()  # --donald is an object in class name = Duck
    donald.quack()
    donald.walk()


if __name__ == '__main__': main()

"""
--------Expected Result: -----
Quaack!
Walking like a duck!
"""