import numpy as np

def game_core_v2(number):
    '''Сначала устанавливатся любое random число, а потом уменьшается или увеличивается его в зависимости от того, больше оно
    или меньше нужного.
    Функция принимает загаданное число и возвращает число попыток'''
    count = 1
    predict = np.random.randint(1,101) #предполагаемое число
    if number > predict:
        subtract = number - predict #разница между загаданным и предполагаемым числом
    else:
        subtract = predict - number
    while number != predict: #проверка на равность загаданного и предполагаемого числа.
        count += 1
        if number > predict: #разница(subtract) делится пополам и целая часть от деления прибавляется к предполагаемому числу, пока оно не станет равным загаданному
            if subtract == 1:
                predict += subtract
            else:
                subtract //= 2
                predict += subtract
        elif number < predict: #разница(subtract) делится пополам и целая часть от деления вычитается от предполагаемого числа, пока оно не станет равным загаданному
            if subtract == 1:
                predict -= subtract
            else:
                subtract //= 2
                predict -= subtract
    return(count) # выход из цикла, если число угадано

def score_game(game_core):
    '''Игра запускается 1000 раз, чтобы узнать, как быстро она угадывает число'''
    count_ls = []
    np.random.seed(1)  # фиксируется RANDOM SEED, чтобы эксперимент был воспроизводим
    random_array = np.random.randint(1,101, size=(1000)) #генерируется 1000 чисел от 1 до 100 для подачи на вход игре
    for number in random_array:
        count_ls.append(game_core(number)) #список заполняется числами, которые показывают, сколько попыток понадобилось, чтобы угадать число
    score = int(np.mean(count_ls)) #среднее количество попыток
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return(score)

score_game(game_core_v2)