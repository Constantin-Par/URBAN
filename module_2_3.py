my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]

int_index = 0

while my_list[int_index] >= 0 and int_index <= len(my_list):

    if my_list[int_index] > 0:
        print(my_list[int_index])

    int_index += 1

# с break

int_index = 0

while True:

    if my_list[int_index] < 0:
        break

    if my_list[int_index] > 0:
        print(int_index, my_list[int_index])

    int_index += 1

    if int_index > len(my_list):
        break
