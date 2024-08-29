from time import sleep


class User:

    def __init__(self, nickname=None, password=None, age=None):
        self.nickname = nickname
        self.password = password
        self.age = age


class Video:
    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode


class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = User()

    def find_user(self, nickname):
        """
        Возвращает пароль пользователя, если пользователь найден
        или значение None если такой пользователь не зарегистрирован
        :param nickname: имя пользователя
        :return: пароль или None
        """
        for user in self.users:
            if user.nickname is nickname:
                return user.password
        return None

    def register(self, nickname, password, age):
        if self.find_user(nickname) is None:
            self.current_user = User(nickname, hash(password), age)
            self.users.append(self.current_user)
            return
        print(f'Пользователь {nickname} уже существует')

    def log_in(self, nickname, password):
        if self.find_user(nickname) is hash(password):
            self.current_user = self

    def log_out(self):
        self.current_user = None

    def find_video(self, title):
        for video in self.videos:
            if title is video.title:
                return video
        return None

    def add(self, *videos):
        for video in videos:
            if self.find_video(video.title) is None:
                self.videos.append(video)

    def get_videos(self, part_of_title):
        result = []
        for video in self.videos:
            if part_of_title.lower() in video.title.lower():
                result.append(video.title)
        return result

    def watch_video(self, title):
        video = self.find_video(title)
        if video is None:
            return
        if self.current_user.nickname is None:
            print('Войдите в аккаунт, чтобы смотреть видео')
            return
        if self.current_user.age < 18 and video.adult_mode:
            print('Вам нет 18 лет, пожалуйста, покиньте страницу')
            return
        for video.time_now in range(1, video.duration + 1):
            print(f'{video.time_now} ', end='')
            sleep(1)
        print('Конец видео')
        video.time_now = 0


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user.nickname)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
