"""
Given a list of postive and negative numbers in random order.
Using O(N) Time and O(1) Space, shift all negative numbers to one side and positive to other side.
Idea is to use 2 pointers, so that from 0...i all values are negative
and from i+1...j all values are positive, and for j+1..n we do not know.
"""

def list_seg(numbers):
    print("#######")
    print("Prev: ", numbers)
    i = 0
    l = len(numbers)
    for j in range(l):
        if numbers[j] < 0:
            numbers[i], numbers[j] = numbers[j], numbers[i]
            i = i + 1
    print("Updated: ", numbers)
    print("#######")
    
if __name__ == "__main__":
    list_seg([-2,-3,4,5,-1])
    list_seg([0,1,1,1,1])
    list_seg([-9,-8])
    list_seg([-4,-5,1])
    list_seg([3,-1,4,-5])
    list_seg([3,-1,4,5])

