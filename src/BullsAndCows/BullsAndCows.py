import pandas as pd
import numpy as np
import random

def main():
    print("Firstly, input the length of the sequence to be stored in memory")
    print("Secondly, keep guessing the number stored in memory. Note: Every guess should be of the same length sequence as declared in step 1")
    print("Keep guessing till you get all the bulls right")
    length = int(input('Input the length of sequence: '))
    ans = generateSeq(length)

    bullseye = False
    count = 0
    while(not bullseye):
        try:
            num = int(input('Enter your Guess of ' + str(length) + ' digit number:'))
            numList = [int(i) for i in str(num)]
            count +=1
            #print(numList
            if len(numList) != length:
                bullseye = False
            else:
                bullseye = checkBullsEye(numList, ans)
        except ValueError:
            print("Sorry, I didn't understand that.")

            # better try again... Return to the start of the loop
            continue

    print("Your guess count is : " + str(count))
    print("You got it right!! Congratulations")
def checkBullsEye(num, ans):
    bulls = 0
    cows = 0
    bullsEye = False
    for i, a in zip(num, ans):
        if i == a:
            bulls +=1
        elif i in ans:
            cows +=1

    print(str(bulls) + " bulls " + str(cows) + " cows")

    if bulls == len(ans):
        bullsEye = True
    return bullsEye

def generateSeq(n):
    num = random.sample(range(0, 9), n)
    if num[0] == 0:
        num = generateSeq(n)
    #print(num
    return num


if __name__ == '__main__':
  main()