# Bubble sort


def bubble_sort(a):
    l = len(a)
    for i in range(l):
        swap_flag = False
        for j in range(l - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swap_flag = True
        if not swap_flag:
            break
    return a


def selection_sort(a):
    l = len(a)
    for i in range(l):
        swap_flag = False
        for j in range(i + 1, l):
            if a[i] > a[j]:
                a[j], a[i] = a[i], a[j]
                swap_flag = True
        if not swap_flag:
            break
    return a


def main():
    a = [1, 5, 3, 2, -1]
    print "Original Array::  %s" % a
    sorted_a = bubble_sort(a)
    print "Bubble Sorted Array::  %s" % sorted_a
    sorted_a = selection_sort(a)
    print "Selection Sorted Array:: %s" % sorted_a

if __name__ == '__main__':
    main()
