from threading import Thread
from time import sleep


class Knight(Thread):
    MAX_ALIENS = 100

    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power
        self.aliens_alive = Knight.MAX_ALIENS
        self.days = 0
        print(f'{self.name}, на нас напали!')

    def run(self):
        while self.aliens_alive > 0:
            self.aliens_alive -= self.power
            self.days += 1
            sleep(1)
            print(f'{self.name} сражается {self.days} дней(дня)..., осталось {self.aliens_alive} воинов.')
            if self.aliens_alive <= 0:
                print(f'{self.name} одержал победу спустя {self.days} дней(дня)!')
                return


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight('Sir Galahad', 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()

print('Все битвы закончились!')
