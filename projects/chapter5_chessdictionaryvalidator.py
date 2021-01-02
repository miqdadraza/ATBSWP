"""
Chess Dictionary Validator
In this chapter, we used the dictionary value {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'} to represent a chess board. Write a function named isValidChessBoard() that takes a dictionary argument and returns True or False depending on if the board is valid.

A valid board will have exactly one black king and exactly one white king. Each player can only have at most 16 pieces, at most 8 pawns, and all pieces must be on a valid space from '1a' to '8h'; that is, a piece can’t be on space '9z'. The piece names begin with either a 'w' or 'b' to represent white or black, followed by 'pawn', 'knight', 'bishop', 'rook', 'queen', or 'king'. This function should detect when a bug has resulted in an improper chess board.

Steps:
1) Exactly 1 black king and exactly one white king

2) Each player can only have at most 16 pieces

3) at most 8 pawns

4) all pieces must be on a valid space from '1a' to '8h'; that is, a piece can’t be on space '9z'.

5 & 6) The piece names begin with either a 'w' or 'b' to represent white or black, followed by 'pawn', 'knight', 'bishop', 'rook', 'queen', or 'king'

"""
import string

def isValidChessBoard(chessboard_dict):
    
    # Step 1: Exactly 1 bking and 1 wking
    
    bking = 0 
    wking = 0
    for piece in chessboard_dict.values(): #checks each value in the dictionary
        if piece == 'bking': #if the value is "bking"
            bking +=1
        if piece == 'wking':
            wking +=1
    if bking > 1 or wking > 1:
        return "Failed step 1"
    
    # Step 2: Each player can only have at most 16 pieces
    whitepieces = 0
    blackpieces = 0
    for w_b in chessboard_dict.values(): #checks each value in the dictionary
        if w_b[0] == 'w': #if the first letter of the value is "w"
            whitepieces +=1
        if w_b[0] == 'b':
            blackpieces +=1
    if whitepieces > 16 or blackpieces > 16:
            return "Failed Step 2"
        
    #Step 3: At most 8 pawns
    whitepawn = 0
    blackpawn = 0
    for pawn in chessboard_dict.values():
        if pawn == "wpawn":
            whitepawn+=1
        if pawn == "bpawn":
            blackpawn+=1
    if whitepawn > 8 or blackpawn > 8:
        return "Failed Step 3"

    #Step 4: all pieces must be on a valid space from '1a' to '8h'; that is, a piece can’t be on space '9z'.
    
    #first going to create a list from 1a - 8h
    allpawns = []
    numbers = [1,2,3,4,5,6,7,8]
    letters = list(string.ascii_lowercase[:8]) #getting a list of letters from a to h
    for i in range(len(numbers)): #first loop for all the numbers
        for j in range(len(letters)): #second loop for all the letters
            allpawns.append(letters[j]+str(numbers[i])) #entering them into empty string
    
    #now going to check if the pieces keys are in the all pawns list
    for pieces in chessboard_dict.keys():
        if pieces not in allpawns:
            return "Failed Step 4"
    

    # Step 5: The piece names beging with either a "w" or "b"
    for i in chessboard_dict.values():
        if i[0] != "b" and i[0] != "w":
            return "Failed Step 5"
    
    #Step 6: followed by 'pawn', 'knight', 'bishop', 'rook', 'queen', or 'king'
    piecenames = ['pawn', 'knight', 'bishop', 'rook', 'queen', 'king']
    for k in chessboard_dict.values():
        if k[1:] not in piecenames:
            return "Failed Step 6"
    
