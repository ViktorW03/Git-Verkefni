#!/usr/bin/env python3

def main():
    l1 = []
    l0 = []
    
    while True:
        word = input().strip().lower()
        
        if word == 'x':
            break
            
        if not l1:
            l1.append(word)
        else:
            if word[0] == l1[-1][-1]:
                l1.append(word)
            else:
                l0.append(word)

    print(' '.join(l1))
    print(' '.join(l0))

if __name__ == "__main__":
    main()
