#!/usr/bin/env python3

def main():
    
    n = int(input())
    m = input().split()

    L = list()
    for i in m:
        L.append(int(i))

    L = sorted(L)

    first_third_length = n // 3

    first_third = L[:first_third_length]
    second_third = L[first_third_length:2*first_third_length]
    third_third = L[2*first_third_length:]

    new_list = second_third + first_third + third_third


    print(' '.join(map(str, new_list)))


if __name__ == "main":
    main()