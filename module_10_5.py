from datetime import datetime
import multiprocessing

def read_info(name):
    all_data = []
    with open(name, 'r') as f:
        while True:
            string = f.readline()
            if string == '':
                return
            all_data.append(string)


if __name__ == '__main__':

    all_files = [f'file {i}.txt' for i in range(1, 5)]

    time_start = datetime.now()
    for file in all_files:
        read_info(file)
    time_finish = datetime.now()
    print(f'Время выполнения линейно: {time_finish - time_start}') 
    # Время выполнения линейно: 0:00:07.014725

    time_start = datetime.now()
    with multiprocessing.Pool(processes=4) as pool:
        pool.map(read_info, all_files)
    time_finish = datetime.now()
    print(f'Время выполнения многопроцессорно: {time_finish - time_start}')
    # Время выполнения многопроцессорно: 0:00:02.744140