import pandas as pd
import numpy as np
import random
import math
from itertools import groupby

def main():
    # create the bingo box with 25 numbers split across a 5x5 matrix
    df = createbingobox()
    print df

    bingo = False
    while(not bingo):
        try:
            num = int(raw_input('Input your number: '))
            # Strike the input number
            df = strike(num, df)
            #Check if five rows are striken
            bingo = checkBingo(df)
            #Suggest numbers for Player 2's move
            mymove = choosenums(df)
            print "Pick the suggested numbers for player 2's move"
            print mymove

            # print bingo
        except ValueError:
            print("Sorry, I didn't understand that.")
            # better try again... Return to the start of the loop
            continue


    print df
    if bingo:
        print "BINGO!! Game over ***"


def choosenums(tempdf):
    dicta = {}
    dictb = {}

    suggested_moves = []
    tempARows = get5X5rows(tempdf)
    #Chooses numbers which are in close proximity to cut the rows
    for row in tempARows:
        dictb[tuple(row)] = sum(not math.isnan(item) for item in row)
    dictb = {k: v for k, v in dictb.items() if v}
    if (min(dictb.itervalues()) < 4):
        xa = [k for k, v in dictb.iteritems() if v == min(dictb.itervalues())]
        for f in xa:
            for i in f:
                if not math.isnan(i):
                    suggested_moves.append(i)
    # Chooses numbers which benefits in cutting two or more rows
    if len(set(suggested_moves)) < len(suggested_moves):
        suggested_moves = [key for key, group in groupby(suggested_moves) if len(list(group)) > 1]
    # Chooses numbers which are located in rich places of the bingo matrix
    if not suggested_moves:
        for i in range(0, len(tempdf)):

            for aa in list('BINGO'):
                temab = tempdf
                # print temab.iloc[i][aa]
                if (not math.isnan(temab.iloc[i][aa])):
                    temab = temab.replace(temab.iloc[i][aa], np.NaN)
                    tempBRows = get5X5rows(temab)
                    dicta[tempdf.iloc[i][aa]] = sum(sum(not math.isnan(item) for item in l) for l in tempBRows)
                    suggested_moves = [k for k, v in dicta.iteritems() if v == min(dicta.itervalues())]
    return suggested_moves


def checkBingo(df):
    bingo = False
    bingoRows = get5X5rows(df)
    print "rows cut " + str(sum(all(math.isnan(item) for item in l) for l in bingoRows) )
    if (sum(all(math.isnan(item) for item in l) for l in bingoRows) >= 5):
        bingo = True
    return bingo

#Selects bingo rows
def get5X5rows(df):
    #get rows in to a temp list
    temp = df.values.tolist()
    #get columns in to a temp list
    for col in df:
        temp.append(df[col].values.tolist())
    #get LHS diagonal elements in a temp list
    temp.append(np.diag(df).tolist())
    # get RHS diagonal elements in a temp list
    rhs = []
    rhs.append(df.iloc[0]['O'])
    rhs.append(df.iloc[1]['G'])
    rhs.append(df.iloc[2]['N'])
    rhs.append(df.iloc[3]['I'])
    rhs.append(df.iloc[4]['B'])
    temp.append(rhs)
    #print temp
    return temp

def strike(num, df_):
    x = int(num)
    df_.replace(x, np.NaN, inplace=True)
    print df_
    return df_

def createbingobox():
    bingoNums = list(range(1, 26))
    n = 5
    looper = list(range(1, n+1))
    df_ = pd.DataFrame(index=list('12345'), columns=list('BINGO'))

    for x in looper:
        fivenums = random.sample(bingoNums, 5)

        ser = pd.Series(fivenums, index=list('BINGO'))
        for n in fivenums:
            bingoNums.remove(n)

        #print "iteration " +  str(x)
        #print bingoNums
        #print fivenums

        df_.loc[str(x)] = ser



    return df_


if __name__ == '__main__':
  main()