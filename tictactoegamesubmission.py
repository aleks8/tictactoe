
def checkWinner(array)->bool:
    if (array[0]==array[1]==array[2]):
        print(f"Player {array[0]} wins!")
        return True
    if (array[3]==array[4]==array[5]):
        print(f"Player {array[3]} wins!")
        return True
    if (array[6]==array[7]==array[8]):
        print(f"Player {array[6]} wins!")
        return True
    if (array[0]==array[3]==array[6]):
        print(f"Player {array[0]} wins!")
        return True
    if (array[1]==array[4]==array[7]):
        print(f"Player {array[1]} wins!")
        return True
    if (array[2]==array[5]==array[8]):
        print(f"Player {array[2]} wins!")
        return True
    if (array[0]==array[4]==array[8]):
        print(f"Player {array[0]} wins!")
        return True
    if (array[2]==array[4]==array[6]):
        print(f"Player {array[2]} wins!")
        return True
    return False

def printArray(array):
    print(f"{array[0]},{array[1]},{array[2]}\n" + 
          f"{array[3]},{array[4]},{array[5]}\n" + 
          f"{array[6]},{array[7]},{array[8]}")

def TicTacToe():
    array = ["1","2","3","4","5","6","7","8","9"]

    print("This is your tic tac toe board:")
    printArray(array)
    print("Note: Players please enter values 1 through 9 or you will miss a turn.")

    for i in range(0,9):
        
        while True:
            try:
                x_choice = int(input("Where do you want to place an X?:"))
                #array[int(x_choice)-1]>0 or array[int(x_choice)-1]<8
                #print(f"{array[int(x_choice)-1]}")
            except:
                print("Please enter values from 1 to 9")
                continue
            else:
                break

        #this isn't working how I want 
        """while True:
            try:
                ((int(x_choice)-1) > 0 and (int(x_choice)-1)<9)
                print("Hello")
            except:
                print("Please enter values from 1 to 9")
                continue
            else:
                break """
        
        if ((int(x_choice)-1) < 0 or (int(x_choice)-1) > 8):
            print(f"You can't place an X outside of the board")
            #continue
        else:
            print(f"Placing an X at: {x_choice}")
            if (array[int(x_choice)-1] == "O"):
                print(f"You can't place an X where there was an O already")
            else: 
                array[int(x_choice)-1] = "X"
        printArray(array)
        if (checkWinner(array) == True):
            break
        
        
        while True:
            try:
                o_choice = int(input("Where do you want to place an O?:"))
            except:
                print("Please enter values from 1 to 9.")
                continue
            else:
                break
        
        if ((int(o_choice)-1) < 0 or (int(o_choice)-1) > 8):
            print(f"You can't place an O outside of the board")
            #continue
        else:
            print(f"Placing an O at: {o_choice}")
            if (array[int(o_choice)-1] == "X"):
                print(f"You can't place an O where there was an X already")
        #could check if the 0 choice already has an X!! and make that
        #a method 
            else:
                array[int(o_choice)-1] = "O"
        if (checkWinner(array) == True):
            break
        printArray(array)
        
    
TicTacToe()