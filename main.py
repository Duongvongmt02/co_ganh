
import imp
import time
#======================================================================

AROUND_ARRAY_EVEN = [(-1,-1,1,1),(-1,0,1,0),(-1,1,1,-1),(0,1,0,-1)]                       
AROUND_ARRAY_ODD = [(-1,0,1,0),(0,1,0,-1)]
AROUND_ARRAY_OUT_X = [(1,0),(-1,0)] # X=0 or X=4
AROUND_ARRAY_OUT_Y = [0,1,0,-1] #Y=0 OR Y=4
POSITION_ARRAY_CORNER = [(0,0),(4,4),(0,4),(4,0)]
SIZE = 5
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

# def checkPosition(position):
#     for coordinate in POSITION_ARRAY_CORNER:
#         if(coordinate == position): return -10; # if coordinate at corner
#     if(position[0] == 0 or position[0] == 4): return 1 # if coordinate y =0 or y=4
#     elif(position[1] == 0 or position[1] == 4): return -1 # if coordinate x=0 or x=4
#     else: return 0 # if coordinate at another

def changeColor(position_above, position_below, state , color):
    state[position_above[0]][position_above[1]] = color
    state[position_below[0]][position_below[1]] = color

def has_carry(position_above,position_below,state,color):
    if(state[position_above[0]][position_above[1]]=='.' or state[position_below[0]][position_below[1]]=='.'): 
        return False
    if(state[position_above[0]][position_above[1]]==color or state[position_below[0]][position_below[1]] == color ):
        return False 
    else: return True

def carry(position,state):
    # check = checkPosition(position)
    deltas=[]
    color='.'
    if((position[0]+position[1])%2==0):
        deltas=AROUND_ARRAY_EVEN
    else: deltas=AROUND_ARRAY_ODD
    for delta in deltas:
        color=state[position[0]][position[1]]
        pos_1 = (position[0] + delta[0],position[1] + delta[1])
        pos_2 = (position[0] + delta[2],position[1] + delta[3])
        if(pos_1[0] >= 0 and pos_1[0] < SIZE and pos_1[1] >=0 and pos_1[1] < SIZE 
            and pos_2[0] >= 0 and pos_2[0] < SIZE and pos_2[1] >=0 and pos_2[1] < SIZE):
            if(has_carry(pos_1,pos_2,state,color)): changeColor(pos_1,pos_2,state,color)
    # if(check == -10): return
    # if(check == -1): 
    #     position_above= [-1,-1]
    #     position_below= [-1,-1]
    #     color=''
    #     color=state[position[0]][position[1]]
    #     position_above[0] = position[0] + AROUND_ARRAY_OUT_X[0][0]
    #     position_above[1] = position[1] + AROUND_ARRAY_OUT_X[0][1]
    #     position_below[0] = position[0] + AROUND_ARRAY_OUT_X[1][0]
    #     position_below[1] = position[1] + AROUND_ARRAY_OUT_X[1][1]   
    #     if(not isOther(position_above,position_below,state,color,check)):
    #         changeColor(position_below,position_above,state,color)
    # if(check == 1):
    #     position_above = [-1,-1]
    #     position_below = [-1,-1]
    #     color = ''
    #     color = state[position[0]][position[1]]
    #     position_above[0] = position[0] + AROUND_ARRAY_OUT_Y[0][0]
    #     position_above[1] = position[1] + AROUND_ARRAY_OUT_Y[0][1]
    #     position_below[0] = position[0] + AROUND_ARRAY_OUT_Y[1][0]
    #     position_below[1] = position[1] + AROUND_ARRAY_OUT_Y[1][1]
    #     if(not isOther(position_above,position_below,state,color,check)):
    #         changeColor(position_below,position_above,state,color)

# def move(current, next , state , color):
    


#======================================================================

# Student SHOULD implement this function to change current state to new state properly
def doit(move, state):
    swapPosition(move,state)
    position=move[1] # assign position by the next move
    carry(position,state)
    new_state = board_copy(state)
    return new_state

#======================================================================
Initial_Board = [
                  ['b', 'b', 'b', 'b', '.'], \
                  ['r', '.', '.', 'r', 'b'], \
                  ['b', 'b', 'b', 'r', '.'], \
                  ['r', '.', 'b', '.', 'b'], \
                  ['r', 'r', '.', 'r', 'r'], \
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
        break;

    print("Game Over")
    if curr_player == a:
        print("The Winner is:", student_b, 'red')
    else:
        print("The Winner is:", student_a, 'blue')

play("co_ganh", "co_ganh")
