import math

def getTimeForDownload(timeTakenForDownload, fs, n, s):
    fs = sorted(fs)
    if(fs[0] == 0):
        fs.pop(0)
    else:
        timeForEachFile = math.floor(s/n)
        timetaken = math.ceil(fs[0]/timeForEachFile)
        fs = [f-fs[0] for f in fs]
        timeTakenForDownload = timeTakenForDownload + timetaken
        fs.pop(0)

    if(len(fs)>0):
        timeTakenForDownload = getTimeForDownload(timeTakenForDownload, fs, len(fs), s)
    else:
        print(timeTakenForDownload)
    return timeTakenForDownload


def main():
    try:
        output = []
        t = int(input('Enter number of test cases: '))
        if (t < 0 or t > 1000):
            raise ValueError("Value of t is beyond the range")
        for tc in range(0, t):
            nooffiles_speed = input('Enter values for n and s: ')
            n, s = (int(x) for x in nooffiles_speed.split())
            print(n, s)
            if(n<0 or n>10000):
                raise ValueError("Value of n is beyond the range")
            if(s<0 or s>30000):
                raise ValueError("Value of s is beyond the range")
            if(n>=s):
                raise ValueError("Value of n is greater than s")
            fileSizes = input('Enter values: ')
            fs = [int(x) for x in fileSizes.split()]
            if(len(fs) != n):
                raise ValueError("The file size input does not match with the total number of files")

            timetakenForDownload  = getTimeForDownload(0, fs, n, s)
            output.append(timetakenForDownload)

        print("Output")
        for o in output:
            print(o)

    except ValueError as e:
        print("Error: ", e)

if __name__ == '__main__':
  main()