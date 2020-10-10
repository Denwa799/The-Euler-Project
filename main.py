def error():
    input("Ошибка. Введите пожалуйста номер корректно. Для возврата в меню нажмите любую кнопку ")
    menu()


def task1():
    nums = list(range(1, 1000))
    length = len(nums)
    i = 0
    addition = 0
    while i < length:
        if nums[i] % 3 == 0 or nums[i] % 5 == 0:
            addition += nums[i]
        i += 1
    print("Сумма чисел от 1 до 1000, кратных 3 или 5 =", addition)
    input("Для возврата в меню нажмите любую кнопку ")
    menu()


def task2():
    fib1 = 0
    fib2 = 0
    fib3 = 1
    addition = 0
    while fib3 < 3000000:
        fib1 = fib2
        fib2 = fib3
        fib3 = fib1 + fib3
        if fib3 % 2 == 0:
            addition += fib3
    print("Сумма четных чисел Фибоначчи ниже 4 миллионов =", addition)
    input("Для возврата в меню нажмите любую кнопку ")
    menu()


def task3():
    def simpleDividers(n):
        answer = 0
        d = 2
        while d * d <= n:
            if n % d == 0:
                answer = d
                n //= d
            else:
                d += 1
        if n > 1:
            answer = n
        return answer

    print("Cамый большой делитель числа 600851475143, являющийся простым числом=", simpleDividers(600851475143))
    input("Для возврата в меню нажмите любую кнопку ")
    menu()


def task4():
    def is_polindrom(num):
        raw = str(num)
        r_num = int(raw[::-1])
        if num == r_num:
            return True
        else:
            return False

    pol = []
    for i in range(10, 1000):
        for j in range(10, 1000):
            if is_polindrom(i * j):
                pol.append(i * j)

    print("Самый большой палиндром, полученный умножением двух трехзначных чисел=", max(pol))
    input("Для возврата в меню нажмите любую кнопку ")
    menu()


def menu():
    print("Введите номер упражнения (от 1 до 4)")
    task = input()
    return {
        "1": task1,
        "2": task2,
        "3": task3,
        "4": task4,
    }.get(task, error)()


menu()
