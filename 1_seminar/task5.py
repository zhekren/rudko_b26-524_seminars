def func(list, k):
    if k < 1:
        raise ValueError('Окно не может быть меньше 1')
    middles = []
    for i in range(len(list)):
        mid = list[i:i+k]
        if len(mid)<k:
            break
        middles.append(sum(mid)//len(mid))
    print(*middles)

list = [int(x) for x in input('Введите список чисел:').split()]
k = int(input('Введите размер окна:'))

func(list, k)