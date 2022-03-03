# coding=utf-8
from generator import Generator


def greet():
    print("Здорово, бездельник.")
    print()
    print("Формат ввода: на каждой строке по 2 числа - номер задания (1 - 26) и их количество")
    print("Если одно и тоже задание было выбрано несколько раз, будет взято последнее введенное количество")
    print("Чтобы прекратить ввод, введи пустую строку")
    print()
    print("Наслаждайся")
    print('----------')


if __name__ == '__main__':
    greet()
    g = Generator()

    dct = {}

    print("№ Кол-во")

    inp = input()

    while inp:
        try:
            task, count = (int(x) for x in inp.split())
            assert 1 <= task <= 26
            assert count >= 0
        except Exception:
            print("Некорректный ввод")
        else:
            dct[task] = count
        inp = input()

    g.run(dct)
