for n in range(3, 21):
    str_pass = ''
    for i in range(1, n):
        for j in range(i + 1, n):
            if n % (i + j) == 0:
                str_pass += f'{i}{j}'

    print(f'{n} - {str_pass}')
