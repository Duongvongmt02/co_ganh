
# ======================== Class Player =======================================
class Player:
    #The size of the state
    SIZE = 5

    MAX_DEEP = 3

    #If the sum of row and column is a odd number, the following type
    #is a delta of posible position
    ODD_NUMBER = [(-1,0),(0,-1),(0,1),(1,0)]

    
    #If the sum of row and column is a even number, the following type
    #is a delta of posible position
    EVEN_NUMBER = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]


    # student do not allow to change two first functions
    def __init__(self, str_name):
        self.str = str_name

    def __str__(self):
        return self.str

    # Student MUST implement this function
    # The return value should be a move that is denoted by a list of tuples:
    # [(row1, col1), (row2, col2)] with:
        # (row1, col1): current position of selected piece
        # (row2, col2): new position of selected piece
    def next_move(self, state):
        result = [(1,0), (1, 1)]
        return result

    def get_next_posible_position(self,state,curPosition):
        if(state[curPosition[0]][curPosition[1]] == '.'):
            return []

        sum = curPosition[0] + curPosition[1]
        posibles = []
        deltas=[]
        if(sum % 2 == 0):
            deltas = Player.EVEN_NUMBER
        else:
            deltas = Player.ODD_NUMBER
        for deta in deltas:
            x = curPosition[0] + deta[0]
            y = curPosition[1] + deta[1]
            if(x >= 0 and x < Player.SIZE and y >= 0 and y < Player.SIZE and state[x][y] == '.'):
                posibles.append((x,y))
        
        return posibles

    def generate_posible_state(self,state,isMyPlayer):
        print('Generate state')

    def change_state(self,state,move):
        print('Change state')

    def status_position(x_position, y_position,color=0):
        print('Status position')

    def changeColor(position_attack, position_changed, color_attack):
        print('Change color')

    