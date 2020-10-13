def error():
    input("Ошибка. Введите пожалуйста номер корректно. Для возврата в меню нажмите любую кнопку ")
    menu()


def task1():
    print("Задача 1")
    print("Если выписать все натуральные числа меньше 10, кратные 3 или 5, то получим 3, 5, 6 и 9. Сумма этих чисел "
          "равна 23.")
    print("Найдите сумму всех чисел меньше 1000, кратных 3 или 5.")
    nums = list(range(1, 1000))
    length = len(nums)
    i = 0
    addition = 0
    while i < length:
        if nums[i] % 3 == 0 or nums[i] % 5 == 0:
            addition += nums[i]
        i += 1
    print(addition)
    input("Для возврата в меню нажмите любую кнопку ")
    menu()


def task2():
    print("Задача 2")
    print("Каждый следующий элемент ряда Фибоначчи получается при сложении двух предыдущих. Начиная с 1 и 2, "
          "первые 10 элементов будут:")
    print("1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...")
    print("Найдите сумму всех четных элементов ряда Фибоначчи, которые не превышают четыре миллиона.")
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
    print(addition)
    input("Для возврата в меню нажмите любую кнопку ")
    menu()


def task3():
    print("Задача 3")
    print("Простые делители числа 13195 - это 5, 7, 13 и 29.")
    print("Каков самый большой делитель числа 600851475143, являющийся простым числом?")

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

    print(simpleDividers(600851475143))
    input("Для возврата в меню нажмите любую кнопку ")
    menu()


def task4():
    print("Задача 4")
    print("Число-палиндром с обеих сторон (справа налево и слева направо) читается одинаково. Самое большое "
          "число-палиндром, полученное умножением двух двузначных чисел – 9009 = 91 × 99.")
    print("Найдите самый большой палиндром, полученный умножением двух трехзначных чисел.")

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

    print(max(pol))
    input("Для возврата в меню нажмите любую кнопку ")
    menu()


def task5():
    print("Задача 5")
    print("2520 - самое маленькое число, которое делится без остатка на все числа от 1 до 10.")
    print("Какое самое маленькое число делится нацело на все числа от 1 до 20?")
    n = 20
    i = 19
    while i > 0:
        if n % i == 0:
            i -= 1
        else:
            n += 20
            i = 19
        if i == 1:
            print(n)
            input("Для возврата в меню нажмите любую кнопку ")
            menu()


def menu():
    print("Введите номер упражнения (от 1 до 5)")
    task = input()
    return {
        "1": task1,
        "2": task2,
        "3": task3,
        "4": task4,
        "5": task5,
    }.get(task, error)()


menu()
