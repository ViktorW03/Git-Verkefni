starting_points = 301
player1 = "Player 1"
player2 = "Player 2"


def points_reaining(remaining_points: list)-> bool:
    return all(x for x in remaining_points)
    # [0, 120] = False
    # [120, 120] = True

def new_score(remaining_points: int, points: int)-> int:
        if points > remaining_points:
            return remaining_points
        return remaining_points -points
    
def main():
    remaining_points = [starting_points, starting_points]
    players = [player1, player2]
    i = 0
    while points_reaining(remaining_points):
        try:
            points = int(input(f"Input points for {players[i]}: "))
            remaining_points[i] = new_score(remaining_points[i], points)
            print(f"{players[i]} remaining points: {remaining_points[i]}")
            i = 1 - i
        except ValueError:
            print("Invalid input!")

    print(f"{players[i-1]} won!")

if __name__ == "__main__":
    main()
