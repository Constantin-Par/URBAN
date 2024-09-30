from random import randint
from threading import Thread, Lock
from time import sleep


class Bank:

    def __init__(self):
        self.balance = 0
        self.lock = Lock()

    def deposit(self):
        for i in range(1, 101):
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            rand_int = randint(50, 500)
            self.balance += rand_int
            print(f'{i} Пополнение: {rand_int}. Баланс: {self.balance}')
            sleep(0.001)

    def take(self):
        for j in range(1, 101):
            rand_int = randint(50, 500)
            print(f'{j} Запрос на снятие {rand_int}')
            if rand_int <= self.balance:
                self.balance -= rand_int
                print(f'Снятие: {rand_int}. Баланс: {self.balance}')
            else:
                print(f'Запрос отклонён, недостаточно средств ({self.balance})')
                self.lock.acquire()
            sleep(0.001)


bk = Bank()

# Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank
th1 = Thread(target=Bank.deposit, args=(bk,))
th2 = Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()

th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')