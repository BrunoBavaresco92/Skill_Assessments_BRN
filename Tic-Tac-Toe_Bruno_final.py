#Rules: X always goes first, then O. The first to get three-in-a-row wins. A stalemate when no moves remain is a tie. User always starts, and the PC goes second

#import pandas as pd
import numpy as np
import time
import random

matrix= np.full((3,3),'-')
round=1

#Initialize matrix

def print_board(r): #This function will print the board
    
    round=r
    print("\n" )
    print(f"------ Round "+ str(round) +" ------")
    print("\n" )
    
    print("\t", end="")
    for j in range(3):
        print(f"Col {j+1}", end='\t')
    print()  # Move to the next line for the matrix content

    for i in range(3):
        print(f"Row {i+1}", end='\t')
        for j in range(3):
            print(" ",matrix[i][j], end='\t')
        print() 
    print("\n" )
    #time.sleep(2)

def ask_user_choice():#This function will ask the user if he/she wants to be 'X' or 'O' and asigns to PC the other pointer
    pc_pointer='o'
    
    while True:
        user_pointer = input("Do you want to be 'X' or 'O': ")
            
        if (user_pointer.lower() in('o','x')):
            if(user_pointer.lower() =='o'):
                pc_pointer = 'x'              
            print(f'You chose: {user_pointer.lower()}')
            return user_pointer.lower(), pc_pointer.lower()
            break    
        else:
            print("Invalid choice, please select X or O")
            continue

def ask_user_position(): #This function ask the user for the position of the pointer and check if the position entered is ok and if that spot is not already occupied
    
    while True:
        try:
            user_x= int(input("Select the row to place the pointer: ")) -1
            user_y= int(input("Select the column to place the pointer: ")) -1
            
            if (0 <=user_x <=3 and 0 <=user_y <=3):
                if (matrix[user_x][user_y]=="-"):
                    print(f"Positions is row "+ str(user_x+1 ) + " and column " + str(user_y +1) )
                    return (user_x, user_y)
                    break
                else:
                    print("This position is already occupied")
            else:
                print("Index out of bounds")
                
        except ValueError:
            print("Please enter a valid integer for row and column")

def update_matrix(x,y,pointer): #This function updates the matrix values (board) with user and PC inputs
    
    matrix[x][y]=pointer

def pc_play(): #This function is the PC playing. It will allocate the pointer randomly in an unocuppied spot

    empty_positions = []
    for i in range(3):
        for j in range(3):
            if matrix[i][j] == '-':
                empty_positions.append((i, j))
    
    if not empty_positions:
        return None
    
    random_position = random.choice(empty_positions)
    return random_position

def check_win(): #This function checks if there's a winner
    
    #Vertical check
    for i in range (3):
            j=0
            if(matrix[j][i]== matrix[j+1][i] == matrix[j+2][i]):
                return  matrix[j][i]  
                
        #Horizontal check
    for i in range (3):
            j=0
            if(matrix[i][j]== matrix[i][j+1] == matrix[i][j+2]):
                return matrix[i][j]  
                
        #Diagonal check
    if(matrix[1][1]== matrix[0][0] == matrix[2][2]):
        return matrix[1][1] 
        
    if(matrix[1][1]== matrix[0][2] == matrix[2][0]):
        return matrix [1][1]
    
    return None 
        

#Main

user_pointer,pc_pointer=ask_user_choice()
r=1
print_board(r)

while True:
    
    #User plays
    
    x,y = ask_user_position()
    update_matrix(x,y,user_pointer)
    
    if(r>=3):
        winner=check_win()
        if(winner=='x' or winner=='o'):
            print_board(r)
            print(f"The winner is "+ str(winner))
            print(("\n" ))
            break
    
    #PC plays
    pc_position= pc_play() 
    if pc_position is not None:
        pc_x, pc_y= pc_position
        update_matrix(pc_x,pc_y,pc_pointer)
        print_board(r)
        r=r+1
    else:
        print_board(r)
        print('It is a tie!')
        break
        
    if(r>=3):
        winner=check_win()
        if(winner=='x' or winner=='o'):
            print(f"The winner is "+ str(winner))
            break

    

        












