import logging
import unittest

class Runner:
    def __init__(self, name, speed=5):
        if isinstance(name, str):
            self.name = name
        else:
            raise TypeError(f'Имя может быть только строкой, передано {type(name).__name__}')
        self.distance = 0
        if speed > 0:
            self.speed = speed
        else:
            raise ValueError(f'Скорость не может быть отрицательной, сейчас {speed}')

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers

class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        try:
            r = Runner(10)
            if not isinstance(r.name, str):
                TypeError(f'Нестроковый тип имени: {r.name}')
            for i in range(10):
                r.run()
            self.assertEqual(r.distance, 100)
            logging.info('"test_run" выполнен успешно')
        except TypeError as err:
            logging.warning(msg='Неверный тип данных для объекта Runner', exc_info=True)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        try:
            r = Runner('Ходун', -5)
            if r.speed < 0:
                ValueError(f'Отрицательная скорость у {r.name}')
            for i in range(10):
                r.walk()
            self.assertEqual(r.distance, 50)
            logging.info('"test_walk" выполнен успешно')
        except ValueError as err:
            logging.warning(msg='Неверная скорость для Runner', exc_info=True)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        r1 = Runner('Бегун')
        r2 = Runner('Ходун')
        for i in range(10):
            r1.run()
            r2.walk()
        self.assertNotEqual(r1.distance, r2.distance)


logging.basicConfig(level=logging.INFO, filemode='w',
                    filename='runner_tests.log', encoding='UTF-8',
                    format='%(asctime)s | %(levelname)s | %(message)s')

first = Runner('Вося', 10)
second = Runner('Илья', 5)
# third = Runner('Арсен', 10)

t = Tournament(101, first, second)
print(t.start())
