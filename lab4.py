from random import randint


def main():
    a = []
    N = input("Введите длину списка для сортировки:")
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
            print("Для сортировки списка укажите длину списка больше 1.")


def create_list(a, N):
    for i in range(N):
        a.append(randint(1, 99))
    print(a)


def bubble_sort(a, N):
    """Sorted list
    >>> bubble_sort([50, 19, 5], 3)
    [5, 19, 50]
    >>> bubble_sort([14, 3, 67, 38, 79], 5)
    [3, 14, 38, 67, 79]
    >>> bubble_sort([58, 47, 2, 15, 24, 67], 7)
     Traceback (most recent call last):
       ...
     IndexError: list index out of range
    """
    for i in range(N - 1):
        for j in range(N - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    print(a)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()
