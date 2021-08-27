class Sport(object):
    def __init__(self, sport):
        print(f'{sport} is an athlete lifestyle')


class Cheerleading(Sport):
    def __init__(self):
        print('Definitely Cheerleading is a sport')
        super().__init__('Cheerleading')


d1 = Cheerleading()
