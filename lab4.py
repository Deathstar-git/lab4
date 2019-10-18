from random import randint


def main():
    a = []
    N = input("Введите длинну списка для сортировки:")
    try:
        Val = int(N)
    except TypeError:
        print("Введено неверное значение!")
    except ValueError:
        print("Введено неверное значение!")
    else:
        N = Val
        if N > 1:
            create_list(a, N)
            bubble_sort(a, N)
        else:
            print("Для сортировки списка укажите длинну списка больше 1.")


def create_list(a, N):
    for i in range(N):
        a.append(randint(1, 99))
    print(a)


def bubble_sort(a, N):
    for i in range(N - 1):
        for j in range(N - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    print(a)


main()
