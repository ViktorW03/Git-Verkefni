def find_allowed_direction(row, column):

    if row == 1 and column == 1:
        print ('You can travel: (N)orth.')
        return ["N"]
    elif row == 1 and column == 2:
        print ('You can travel: (N)orth or (E)ast or (S)outh.')
        return ["N", "E" ,"S"]
    elif row == 1 and column == 3:
        print('You can travel: (E)ast or (S)outh.')
        return ["S", "E"]
   
    elif row == 2 and column == 1:
        print ('You can travel: (N)orth.')
        return ["N"]
    elif row == 2 and column == 2:
        print('You can travel: (S)outh or (W)est.')
        return ["S", "W"]
    elif row == 2 and column == 3:
        print('You can travel: (E)ast or (W)est.')
        return ["W", "E"]
    elif row == 3 and column == 2:
        print('You can travel: (N)orth or (S)outh.')
        return ["N", "S"]
    elif row == 3 and column == 3:
        print("You can travel: (S)outh or (W)est.")
        return ["S", "W"]
    
    else:
        return []

def change_coor(row, column, dir):
    if dir == "N":
        column += 1
        return row, column
    elif dir == "S":
        column -= 1
        return row, column
    elif dir == "E":
        row += 1
        return row, column
    elif dir == "W":
        row -= 1
        return row, column
    # elif dir == "S":
    #     column -= 1
    #     return row, column

    
        


def main():
    row, column = 1, 1
    total_coins = 0
    while not (row == 3 and column == 1):
        allow_dir = find_allowed_direction(row, column)
        dir = input("Direction: ").upper()
        valid_move = False
        if dir in allow_dir:
            valid_move = True
            row, column = change_coor(row, column, dir)
        else:
            print("Not a valid direction!")

        lev_possitions= [(1,2), (2,2), (2,3), (3,2)]
        pull_lev = ""
        if (row, column) in lev_possitions and valid_move:
                pull_lev = input("Pull a lever (y/n): ").upper()
                if pull_lev == "Y":
                    total_coins += 1
                    print(f"You received 1 coin, your total is now {total_coins}.")

    print(f"Victory! Total coins {total_coins}.") 




if __name__ == "__main__":
    main()