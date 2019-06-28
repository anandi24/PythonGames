import math
import collections

def main():
  #size = int(input('Input the length of board: '))
  size = 3
  goalList = list(range(0, int(math.pow(size, 2))))
  #print(goalList)
  #search_initialState = input('Input the search criteria aith the initial position')
  print("dfs ", bfs([1,2,5,3,4,0,6,7,8],goalList, size))

def bfs(initialStage, goalState, size):
    frontier = collections.deque()
    frontier.append(initialStage)
    explored = []
    depth = 0
    while frontier:
        state = frontier.popleft()
        explored.append(state)
        print("frontire ", frontier)
        print("explored ", explored)
        if(goalState == state):
            print("depth ", depth)
            return True
        else:
            parent = {}
            path = []
            for dir in ["up", "down", "left", "right"]:
                newState = []
                newState = swapDirection(state, size, dir)
                if newState not in frontier and newState not in explored:
                    path.append(dir)
                    frontier.append(newState)
                parent[str(state)] = path
            print("parent", parent)
    return False

def dfs(initialStage, goalState, size):
    frontier = []
    frontier.append(initialStage)
    explored = []

    while frontier:
        state = frontier.pop()
        explored.append(state)
        print("frontire ", frontier)
        print("explored ", explored)
        if(goalState == state):
            print(len(explored))
            return True
        else:
            parent = {}
            path = []
            for dir in ["up", "down", "left", "right"]:
                newState = []
                newState = swapDirection(state, size, dir)
                if newState not in frontier and newState not in explored:
                    path.append(dir)
                    frontier.append(newState)
                parent[str(state)] = path
            print("parent", parent)
    return False


def swapDirection(board, size, direction):
    print("before swapping ", board)
    zeropos = (board.index(0))
    tempBoard = list(board)
    if(direction=="left"):
        if (zeropos in [(x * size) for x in range(0, size)]):
            print("swapping left cell is not possible")
        else:
            tempBoard[zeropos], tempBoard[zeropos - 1] = board[zeropos - 1], board[zeropos]
    elif(direction == "right"):
        if (zeropos in [((x + 1) * size) - 1 for x in range(0, size)]):
            print("swapping right cell is not possible")
        else:
            tempBoard[zeropos], tempBoard[zeropos + 1] = board[zeropos + 1], board[zeropos]
    elif(direction == "down"):
        if (zeropos in [x + (size * (size - 1)) for x in range(0, size)]):
            print("swapping down cell is not possible")
        else:
            tempBoard[zeropos], tempBoard[zeropos + 3] = board[zeropos + 3], board[zeropos]
    elif(direction == "up"):
        if (zeropos in [x for x in range(0, size)]):
            print("swapping up cell is not possible")
        else:
            tempBoard[zeropos], tempBoard[zeropos - 3] = board[zeropos - 3], board[zeropos]
    print(direction, "temp " , tempBoard, "board ", board)
    return tempBoard

if __name__ == '__main__':
  main()