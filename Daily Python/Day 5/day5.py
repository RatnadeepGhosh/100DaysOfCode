# A SCRIPT THAT WILL CALCULATE MEAN,MEDIAN,MODE,RANGE AND FREQUENCY
#
#

from collections import Counter

#Mean

def mean(*args):
    #finding the sum of all the numbers

    args.sort()

    total_sum = sum(args)

    length = len(args)

    mean = total_sum / length

    return mean

#Median
def median(*args):
    N = len(args)   #finding the lenght of numbers arguments

    #if the length is even then you add the two mid numbers and divide by 2
    if N % 2 == 0:
        m1 = N / 2  # First middle number

        m2 = (N / 2) + 1

        median = (m1 + m2) / 2

    else:
        median = (N + 1) / 2

    return median

#Mode
def mode(*args):
    c = Counter(args)

    mode = c.most_common(1) #return only the number that appears most

    return mode[0][0]

#Range
def range(*args):
    args.sort

    lowest = args[0]

    highest = args[-1]

    range = highest - lowest

    return range

#Frequency
def frequency(*args):
    table = Counter(args)

    print("NUMBERS\tFREQUENCY")

    for number in table.most_common:
        print(number[0],'\t',number[1])


    


#s = mean(23,3,4,5,6,7,8,9,3,67)
#print(s)