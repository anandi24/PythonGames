import pandas as pd
import math

def main():
    df = pd.DataFrame(index=list('123'), columns=list('ABC'))
    player1move = True
    while (player1move):
        try:
            print("Player 1 move")
            print(df.loc['2']['B'])
            move1row, move1col = raw_input('Input your row and column : ').split(' ')
            print(move1col, move1row)
            putX(df, move1col, move1row)
            player2move(df)
            print(df)
        except ValueError:
            print("Sorry, I didn't understand that.")
            # better try again... Return to the start of the loop
            continue

    print(df)

def putX(df_, move1col, move1row):
    df_.loc[move1row][move1col] = 'X'
    return df_

def player2move(df_):
    if(math.isnan(df_['2']['B'])):
        df_.loc['2']['B'] = 'O'
    return df_

if __name__ == '__main__':
  main()
