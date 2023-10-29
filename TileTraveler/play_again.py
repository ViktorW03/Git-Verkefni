
import sys 

lev_possitions= [(1,2), (2,2), (2,3), (3,2)]

def find_allowed_direction(row, column):
    messages = {
        (1, 1): "You can travel: (N)orth.",
        (1, 2): "You can travel: (N)orth or (E)ast or (S)outh.",
        (1, 3): "You can travel: (E)ast or (S)outh.",
        (2, 1): "You can travel: (N)orth.",
        (2, 2): "You can travel: (S)outh or (W)est.",
        (2, 3): "You can travel: (E)ast or (W)est.",
        (3, 2): "You can travel: (N)orth or (S)outh.",
        (3, 3): "You can travel: (S)outh or (W)est."
    }

    directions = {
        (1, 1): ["N"],
        (1, 2): ["N", "E", "S"],
        (1, 3): ["E", "S"],
        (2, 1): ["N"],
        (2, 2): ["S", "W"],
        (2, 3): ["E", "W"],
        (3, 2): ["N", "S"],
        (3, 3): ["S", "W"]
    }

    print(messages.get((row, column)))
    return directions.get((row, column), [])

def change_coor(row, column, dir):
    if dir == "N":
        column += 1
    elif dir == "S":
        column -= 1
    elif dir == "E":
        row += 1
    elif dir == "W":
        row -= 1

    return row, column

def get_coins(row, column, total_coins):
    if (row, column) in lev_possitions:
        pull_lev = input("Pull a lever (y/n): ").upper()
        if pull_lev == "Y":
            total_coins += 1
            print(f"You received 1 coin, your total is now {total_coins}.")
    return total_coins

def move():
    row, column = 1, 1
    total_coins = 0
    while not (row == 3 and column == 1):
        allow_dir = find_allowed_direction(row, column)
        dir = input("Direction: ").upper()
        if dir in allow_dir:
            row, column = change_coor(row, column, dir)
            total_coins = get_coins(row, column, total_coins)
        else:
            print("Not a valid direction!")
        
    return total_coins

def main():
    play_again = "Y"
    while play_again == "Y":
        total_coins = move()
        print(f"Victory! Total coins {total_coins}.")
        play_again = input("Play again (y/n): ").upper()

if __name__ == "__main__":
    main()