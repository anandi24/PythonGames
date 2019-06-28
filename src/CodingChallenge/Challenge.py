def  findNumber(l, r):
    arr = [i for i in range(l, r+1) if((i%2)!=0)]
    print(arr)

if __name__ == '__main__':
    findNumber(3, 5)