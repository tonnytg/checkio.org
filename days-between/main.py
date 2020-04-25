import datetime

def days_diff(A, B):
    print(A)
    print(B)
    #YYYY, M, D
    #https://docs.python.org/library/datetime
    #class datetime.datetime
    #A combination of a date and a time. Attributes: year, month, day, hour, minute, second, microsecond, and tzinfo.
    value = str((datetime.datetime(1982, 4, 1) - datetime.datetime(1982, 4, 22) )).split(' ')
    print(int(value[0])*-1)

    #print(datetime.strftime(%a).date(1982, 4, 19) - datetime.strftime(%a).date(1982, 4, 19) )
    #print(datetime(*(time.strptime(a, '%d')[0:6])))




if __name__ == '__main__':
    #print("Example:")
    #print(days_diff((1982, 4, 19), (1982, 4, 22)))

    days_diff((1982, 4, 19), (1982, 4, 22)) == 3
    #days_diff((2014, 1, 1), (2014, 8, 27)) == 238
    #days_diff((2014, 8, 27), (2014, 1, 1)) == 2381982, 4, 22
    #print("Coding complete? Click 'Check' to earn cool rewards!")1982, 4, 22