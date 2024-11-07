import unittest


class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
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
                    finishers[place] = participant.name
                    place += 1
                    self.participants.remove(participant)

        return finishers


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        r = Runner('Бегун')
        for i in range(10):
            r.run()
        self.assertEqual(r.distance, 100)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        r = Runner('Ходун')
        for i in range(10):
            r.walk()
        self.assertEqual(r.distance, 50)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        r1 = Runner('Бегун')
        r2 = Runner('Ходун')
        for i in range(10):
            r1.run()
            r2.walk()
        self.assertNotEqual(r1.distance, r2.distance)


class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = dict()

    @classmethod
    def tearDownClass(cls):
        [print(f'Tournament Test {k}: {v}') for k, v in cls.all_results.items()]

    def setUp(self):
        self.r1 = Runner('Усэйн', 10)
        self.r2 = Runner('Андрей', 9)
        self.r3 = Runner('Ник', 3)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test1_start(self):
        self.all_results[1] = Tournament(90, self.r1, self.r3).start()
        self.assertTrue(self.all_results[1][2] == self.r3)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test2_start(self):
        self.all_results[2] = Tournament(90, self.r2, self.r3).start()
        self.assertTrue(self.all_results[2][2] == self.r3)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test3_start(self):
        self.all_results[3] = Tournament(90, self.r1, self.r2, self.r3).start()
        self.assertTrue(self.all_results[3][3] == self.r3)

    # def test_start_speed(self):
    #     '''
    #     Дополнительная проверка - здесь будет ошибка.
    #     Независимо от того, в каком порядке передать всех бегунов в Tournament.start(),
    #     на одинаковой дистанции придти они должны в порядке: Усэйн, Андрей, Ник.
    #     На дистанции 90 и меньше баг - Андрей приходит быстрее Усэйна, хотя Усэйн быстрее.
    #     В обходе по self.participants в start() есть баг - если прибежали оба, то первым считается тот,
    #     кто "левее" в списке, а не тот, кто пробежал full_distance быстрее.
    #     Как вариант - надо в конце по всем смотреть "выбег" в метрах за финиш, потом распределять места.
    #     Кто больше "выбежал", тот и выше на ступеньке.
    #     Или объекты в self.participants перед циклом в start() отсортировать по убыванию атрибута Runner.speed.
    #     '''
    #     self.all_results[4] = Tournament(90, self.r2, self.r3, self.r1).start()
    #     self.assertTrue(self.all_results[4][1] == self.r1 and self.all_results[4][2] == self.r2 and
    #                     self.all_results[4][3] == self.r3)
