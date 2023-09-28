#!/usr/bin/env python3

def main():
    n, k = map(int,input().split())
    bags = list (map(int, input().split()))

    index = bags.index(k)

    if index == 0:

        print("fyrst")
    elif index == 1:
        print("naestfyrst")
    else:
        print(f"{index+1} fyrst")

        
        
    


if __name__ == "__main__":
    main()