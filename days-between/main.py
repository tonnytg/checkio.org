import datetime

def days_diff(A, B):
    print( A[0], A[1], A[2])
    # A = int(A)
    # B = int(B)
    #YYYY, M, D
    #https://docs.python.org/library/datetime
    #class datetime.datetime
    #A combination of a date and a time. Attributes: year, month, day, hour, minute, second, microsecond, and tzinfo.
    value = str((datetime.datetime( A[0],A[1],A[2] ) - datetime.datetime( B[0],B[1],B[2] ))).split(' ')
    try:
        print(abs(int(value[0])))
    except ValueError:
        print(0)



if __name__ == '__main__':
    #print("Example:")
    #print(days_diff((1982, 4, 19), (1982, 4, 22)))

    days_diff((1982, 4, 19), (1982, 4, 22)) == 3
    #days_diff((2014, 1, 1), (2014, 8, 27)) == 238
    #days_diff((2014, 8, 27), (2014, 1, 1)) == 2381982, 4, 22
    #print("Coding complete? Click 'Check' to earn cool rewards!")1982, 4, 22
    days_diff((2014, 2, 28), (2014, 2, 28))