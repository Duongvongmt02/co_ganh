
import imp
import time
#======================================================================

AROUND_ARRAY_EVEN = [(-1,-1,1,1),(-1,0,1,0),(-1,1,1,-1),(0,1,0,-1)]                       
AROUND_ARRAY_ODD = [(-1,0,1,0),(0,1,0,-1)]
AROUND_ARRAY_X = [(0,1),(0,-1)] # X=0
AROUND_ARRAY_Y = [1,0,-1,0] #Y=0
POSITION_ARRAY_CORNER = [(0,0),(4,4),(0,4),(4,0)]

def board_print(board, move=[], num=0):

    print("====== The current board(", num, ")is (after move): ======")
    if move:
        print("move = ", move)
    for i in [4, 3, 2, 1, 0]:
        print(i, ":", end=" ")
        for j in range(5):
            print(board[i][j], end=" ")
        print()
    print("   ", 0, 1, 2, 3, 4)
    print("")


def board_copy(board):
    new_board = [[]]*5
    for i in range(5):
        new_board[i] = [] + board[i]
    return new_board

def swapPosition(next_move,state):
    temp=state[next_move[0][0]][next_move[0][1]]
    state[next_move[0][0]][next_move[0][1]]=state[next_move[1][0]][next_move[1][1]]
    state[next_move[1][0]][next_move[1][1]]=temp

def checkPosition(position):
    for coordinate in POSITION_ARRAY_CORNER:
        if(coordinate == position): return -10; # if coordinate at corner
    if(position[0] == 0): return -1 # if coordinate x =0
    elif(position[1] == 0): return 1 # if coordinate y = 0
    else: return 0 # if coordinate at another

def changeColor(position_1, position_2, state , color):
    state[position_1[0]][position_1[1]] = color
    state[position_2[0]][position_2[1]] = color

def isOther(position_above,position_below,state,color,check):
    if(check==-1):
            if(state[position_above[0]][position_above[1]]==color and state[position_below[0]][position_below[1]] == color):
                return true; 


def carry(position,state):
    check = checkPosition(position)
    if(check == -10): return
    if(check == -1): 
        color=state[position[0]][position[1]]
        position_above = position + AROUND_ARRAY_X[0]
        position_below = position - AROUND_ARRAY_X[1]   
        if(isOther(position_above,position_below,state,check)):
            changeColor(position_below,position_above,state,color)


# def move(current, next , state , color):
    


#======================================================================

# Student SHOULD implement this function to change current state to new state properly
def doit(move, state):
    swapPosition(move,state)
    position=move[1]
    carry(position,state)
    new_state = board_copy(state)
    return new_state

#======================================================================
Initial_Board = [
                  ['b', 'b', 'b', 'b', 'b'], \
                  ['b', '.', '.', '.', 'b'], \
                  ['b', '.', '.', '.', 'r'], \
                  ['r', '.', '.', '.', 'r'], \
                  ['r', 'r', 'r', 'r', 'r'], \
                ]

# 4 : r r r r r
# 3 : r . . . r
# 2 : b . . . r
# 1 : b . . . b
# 0 : b b b b b
#     0 1 2 3 4
#======================================================================

def check_winner(state):
    red = 0
    blue = 0
    for i in range(len(state)) :
        for j in  range(len(state[i])):
            if(state[i][j] == 'b'):
                blue+=1
            if (state[i][j] == 'r'):
                red+=1
    if (red == 0) :
        return 'b'
    elif (blue == 0):
        return 'r'
    else :
        return

def play(student_a, student_b, start_state=Initial_Board):
    player_a = imp.load_source(student_a, student_a + ".py")
    player_b = imp.load_source(student_b, student_b + ".py")

    a = player_a.Player('b')
    b = player_b.Player('r')
    
    curr_player = a
    state = start_state    

    board_num = 0
        
    board_print(state)
    
    while True:
        print("It is ", curr_player, "'s turn")

        start = time.time()
        move = curr_player.next_move(state)
        print('Next available position', curr_player.get_next_posible_position(state,(0,2)))
        elapse = time.time() - start

        # print(move)

        if not move:
            break

        print("The move is : ", move, end=" ")
        print(" (in %.2f ms)" % (elapse*1000), end=" ")
        if elapse > 3.0:
            print(" ** took more than three second!!", end=" ")
            break
        print()
        # check_move
        state = doit(move, state)

        board_num += 1
        board_print(state, num=board_num)

        if curr_player == a:
            curr_player = b
        else:
            curr_player = a

    print("Game Over")
    if curr_player == a:
        print("The Winner is:", student_b, 'red')
    else:
        print("The Winner is:", student_a, 'blue')

play("co_ganh", "co_ganh")
