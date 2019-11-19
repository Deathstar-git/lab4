from random import randint


def test_sort():
    assert bubble_sort([]) == []
    assert bubble_sort([12]) == [12]
    assert bubble_sort([56, 56]) == [56, 56]
    assert bubble_sort([17, 25, -67, 74, -89]) == [-89, -67, 17, 25, 74]
    assert bubble_sort([56, 9, 48, 99, 13, 67]) == [9, 13, 48, 56, 67, 99]


def main():
    a = []
    N = input("Введите длину списка для сортировки:")
    try:
        Val = int(N)
    except (TypeError, ValueError):
        print("Введено неверное значение!")
    else:
        N = Val
        if N > 1:
            for i in range(N):
                a.append(randint(1, 99))
            print(a)
            bubble_sort(a)
        else:
            print("Для сортировки списка укажите длину списка больше 1.")


def bubble_sort(a):
    """Sorted list
    >>> bubble_sort([50, 19, 5])
    [5, 19, 50]
    >>> bubble_sort([14, 3, 67, 38, 79])
    [3, 14, 38, 67, 79]
    >>> bubble_sort([58, 47, 2, 15, 24, 67])
    [2, 15, 24, 47, 58, 67]
    """
    for i in range(len(a) - 1):
        for j in range(len(a) - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a


if __name__ == '__main__':
    main()
