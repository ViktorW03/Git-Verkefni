Queen = 9
Rook = 5
Bishop = 3
Knight = 3
Pawa = 1

chess_piece = int(input())

if chess_piece == 9:
    print ("Queen")
elif chess_piece == 5:
        print ("Rook")
elif chess_piece == 3:
            print ("Bishop or Knight")
elif chess_piece == 1:
                print ("Pawn")
else:
                print ("No piece")
                
                
            