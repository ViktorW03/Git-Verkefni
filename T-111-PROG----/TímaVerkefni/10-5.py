#!/usr/bin/env python3

def main():
    homeworks = input().split(";")
    counter = 0
    for homework in homeworks:
        if "-" in homework:
            start,end = homework.split("-")
            total = int(end)+1-int(start)
            counter += total
        else:
            counter += 1
    print(counter)

if __name__ == "__main__":  
    main()
