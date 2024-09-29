from datetime import datetime
from threading import Thread
from time import sleep


def write_words(word_count, file_name):
    with open(file_name, 'w', encoding='windows-1251') as current_file:
        for i in range(1, word_count + 1):
            current_file.write(f'Какое-то слово № {i}\n')
            sleep(0.1)
        print(f'Завершилась запись в файл {file_name}')


time_start = datetime.now()
write_words(10, 'example_10_1.txt')
write_words(30, 'example_10_2.txt')
write_words(200, 'example_10_3.txt')
write_words(100, 'example_10_4.txt')
print('Один поток:',datetime.now() - time_start)

time_start = datetime.now()

t_1 = Thread(target=write_words, args=(10, 'example_10_5.txt'))
t_2 = Thread(target=write_words, args=(30, 'example_10_6.txt'))
t_3 = Thread(target=write_words, args=(200, 'example_10_7.txt'))
t_4 = Thread(target=write_words, args=(100, 'example_10_8.txt'))

t_1.start()
t_2.start()
t_3.start()
t_4.start()

t_1.join()
t_2.join()
t_3.join()
t_4.join()

print('Четыре потока:',datetime.now() - time_start)
