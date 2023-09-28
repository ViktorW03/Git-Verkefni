#!/usr/bin/env python3

def main():
    n = int(input())

    numbers = [int(input()) for _ in range(n)]

    for num in reversed(numbers):
        print(num)

    # implement your code here


if __name__ == "__main__":
    main()
