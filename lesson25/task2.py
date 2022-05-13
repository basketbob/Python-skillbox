import random


class Error(Exception):
    def __init__(self, message):
        file = open('karma.log', 'a')
        file.write(message)
        self.message = message


class KillError(Error):
    def __init__(self):
        super().__init__('Kill error\n')


class DrunkError(Error):
    def __init__(self):
        super().__init__('Drunk error\n')


class CarCrashError(Error):
    def __init__(self):
        super().__init__('Car crash error\n')


class GluttonyError(Error):
    def __init__(self):
        super().__init__('Gluttony error\n')


class DepressionError(Error):
    def __init__(self):
        super().__init__('Depression error\n')


class Life:
    KARMA = 500
    crnt_karma = 0
    excpt = 0

    def check_karma(self):
        god = False
        if self.KARMA <= self.crnt_karma:
            god = True

        return god

    def one_day(self):
        cnt_karma = random.randint(1, 7)
        error = random.choice([KillError, DrunkError, CarCrashError, GluttonyError, DepressionError])
        try:
            if self.excpt > 8:
                self.excpt = 0
                raise error
            else:
                self.excpt += 1
        except error:
            pass

        return cnt_karma


life = Life()
file = open('karma.log', 'w')
file.close()
cnt = 0
while True:
    life.crnt_karma += life.one_day()

    if life.crnt_karma >= life.KARMA:
        print('500 level done!')
        break
