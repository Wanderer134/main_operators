n = int(input('Введите число от 3 до 20: '))

if n < 3 or n > 20:
    print('Число должно быть в диапазоне от 3 до 20.')
else:
    numbers = list(range(1, 20))
    result = ''

    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            pair_sum = numbers[i] + numbers[j]
            if n % pair_sum == 0:
                result += f"{numbers[i]}{numbers[j]}"
    print("Нужный пароль:", result)







